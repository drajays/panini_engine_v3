"""
engine/resolver.py — Rule-conflict resolver (Constitution Art. 21).
────────────────────────────────────────────────────────────────────

Runtime conflict is Ladder 1 of AMENDMENT 17, in order. A commentary is never
consulted here (Art. 22 is design-time only).

  pre-conflict (gates, not this module): pāṭha / asiddhatva / pratiṣedha /
  nipātana-freeze.

  In this module, of the candidates the scheduler still offers:

    1. named override / jñāpaka   (CONFLICT_OVERRIDES — an amendment)
    2. declared apavāda           (PŚ 57; SutraRecord.apavada_of)
    3. vibhāṣā stop               (fork; do not pick)
    4. nitya, antaraṅga           (PŚ 38; declared not_modelled → Art. 18 gap)
    5. para                       (1.4.2 / PŚ 38 — Pāṇini's floor)

Rajpopat SOI is a *diagnostic*. If it would have picked a different winner than
*para*, that is recorded as ``undeclared_apavada_candidate``. It never wins
(Art. 21: no unnamed heuristic may be a winner).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, FrozenSet, List, Optional

from engine.phase import is_tripadi_sutra
from engine.paribhasha import layer as paribhasha_layer
from engine.paribhasha import not_modelled as unmodelled_layers
from engine.registry   import get_sutra
from engine.state      import State
from engine.sutra_type import SutraRecord, SutraType


# Named overrides. Populated only by explicit amendment in docs/ (Art. 21 L10).
CONFLICT_OVERRIDES: Dict[FrozenSet[str], str] = {
    # Example shape:
    # frozenset({"1.1.3", "6.1.87"}): "6.1.87",
    frozenset({"6.1.17", "7.4.60"}): "6.1.17",     # docs/AMENDMENT_19.md: abhyāsa samprasāraṇa before halādiḥ śeṣaḥ
    frozenset({"6.4.101", "6.4.119"}): "6.4.101",     # docs/AMENDMENT_19.md: एधि — hi→dhi after the jhal-final as, then e
    frozenset({"6.1.50", "7.3.84"}): "6.1.50",       # docs/AMENDMENT_19.md: dāsyate, mātā — ātva before guṇa (data: ashtadhyayi.com dhātu table)
    frozenset({"6.1.50", "7.2.1"}): "6.1.50",        # amāsīt, not *amaiṣīt
    frozenset({"7.2.3", "7.2.73"}): "7.2.73",       # docs/AMENDMENT_19.md: anaMsIt — sak+iṭ first, then 7.2.4 forbids the vṛddhi of 7.2.3
    frozenset({"6.1.8", "6.1.45"}): "6.1.45",       # docs/AMENDMENT_19.md: glai/ṣṭyai/vai liṭ — ātva on the bare root, then dvitva (jaglau)
    frozenset({"7.3.96", "7.4.50"}): "7.3.96",     # docs/AMENDMENT_19.md: आसीः — īṭ comes first, so the two s's are no longer adjacent
}

# Decision.layer values Art. 21 permits. Constitutional test greps this set.
DECISION_LAYERS: FrozenSet[str] = frozenset({
    "sole-candidate",
    "override",
    "jnapaka",
    "upadesha",
    "asiddha",
    "pratishedha",
    "antaranga",
    "purva",
    "apavada",
    "vikalpa",
    "para",
})


_DECIDES: list[bool] = [False]


class resolver_decides:
    """Context manager: while a derivation is driven by the resolver (the subanta scanner, the
    autonomous loop), a rule must not pre-judge its rivals — 6.1.97 used to decline by itself when a
    later rule also applied (ROADMAP C2/C4, Art. 15). Recipe pipelines, which have no resolver, still
    rely on that self-narrowing; it disappears with the last of them."""

    def __enter__(self):
        self._prev = _DECIDES[0]
        _DECIDES[0] = True

    def __exit__(self, *exc):
        _DECIDES[0] = self._prev


def decides() -> bool:
    return _DECIDES[0]


class UnresolvedConflict(RuntimeError):
    """All resolver layers failed to pick a unique winner."""


@dataclass(frozen=True)
class Decision:
    """Who won, by which paribhāṣā, and who lost."""

    winner: str
    layer: str                       # must be in DECISION_LAYERS
    reason_dev: str
    losers: tuple[str, ...] = field(default_factory=tuple)
    skipped_unmodelled: tuple[str, ...] = field(default_factory=tuple)
    soi_proposal: Optional[str] = None

    def gate_reason(self, loser: str) -> str:
        return f"{self.layer}: {self.winner} beat {loser} — {self.reason_dev}"


def _id_key(sid: str) -> tuple[int, ...]:
    return tuple(int(p) for p in sid.split("."))


def _apavada_winner(candidate_ids: List[str]) -> Optional[str]:
    """A declared अपवाद defeats the उत्सर्ग it names, wherever either stands."""
    exceptions = [
        cid for cid in candidate_ids
        if any(other in (get_sutra(cid).apavada_of or ()) for other in candidate_ids)
    ]
    return exceptions[0] if len(exceptions) == 1 else None


def _term_sig(term) -> tuple:
    return ("".join(v.slp1 for v in term.varnas), frozenset(term.tags),
            tuple(sorted((k, repr(v)) for k, v in term.meta.items())))


def _changed_terms(sid: str, state: State) -> frozenset[int]:
    """Indices of the terms a rule would rewrite (all from the first difference on
    if it inserts or removes a term)."""
    from engine.scheduler import probe

    try:
        after = probe(sid, state)
    except Exception:
        return frozenset()
    a, b = state.terms, after.terms
    if len(a) != len(b):
        first = next((i for i in range(min(len(a), len(b))) if _term_sig(a[i]) != _term_sig(b[i])),
                     min(len(a), len(b)))
        return frozenset(range(first, max(len(a), len(b))))
    return frozenset(i for i in range(len(a)) if _term_sig(a[i]) != _term_sig(b[i]))


def _reach(sid: str, state: State) -> int:
    """How far to the right a rule's nimitta extends: the smallest k such that
    ``cond`` is already true with every term after ``k`` cut away."""
    rec = get_sutra(sid)
    for k in range(len(state.terms)):
        cut = state.fork()
        cut.terms = cut.terms[: k + 1]
        try:
            if rec.cond(cut):
                return k
        except Exception:
            continue
    return len(state.terms) - 1


def _zones(candidate_ids: List[str], state: State) -> dict:
    """candidate → (terms it would rewrite, how far right its nimitta reaches); rules that would
    rewrite nothing are absent."""
    info = {}
    for cid in candidate_ids:
        changed = _changed_terms(cid, state)
        if changed:
            info[cid] = (frozenset(changed), _reach(cid, state))
    return info


def _bahiranga_losers(candidate_ids: List[str], state: State, info: dict | None = None) -> set[str]:
    """PŚ 50 असिद्धं बहिरङ्गमन्तरङ्गे. Two rules *contend* when the terms they rewrite
    overlap. Of two that contend, the one whose nimitta
    reaches a term the other does not need is bahiraṅga and yields."""
    info = info if info is not None else _zones(candidate_ids, state)
    losers: set[str] = set()
    for c, (zone_c, reach_c) in info.items():
        for r, (zone_r, reach_r) in info.items():
            if r != c and zone_c & zone_r and reach_r > reach_c:
                losers.add(r)
    return losers


def _soi_proposal(
    candidate_ids: List[str],
    state: State,
    specificity: Optional[Dict[str, Callable[[State], int]]],
) -> Optional[str]:
    """The sūtra SOI *would* have picked — diagnostic only, never a winner."""
    try:
        from engine.specificity_registry import get_specificity
    except ModuleNotFoundError:
        def get_specificity(_sutra_id: str, _state: State) -> int:  # type: ignore[misc]
            return 0

    scores: Dict[str, int] = {}
    for cid in candidate_ids:
        fn = (specificity or {}).get(cid)
        if fn is not None:
            scores[cid] = fn(state)
            continue
        registered = get_specificity(cid, state)
        scores[cid] = registered if registered > 0 else _default_specificity(get_sutra(cid))
    if not scores:
        return None
    top = max(scores.values())
    contenders = [cid for cid, score in scores.items() if score == top]
    return contenders[0] if len(contenders) == 1 else None


def _skipped_unmodelled() -> tuple[str, ...]:
    return tuple(item.key for item in unmodelled_layers())


def resolve_with_reason(
    candidate_ids : List[str],
    state         : State,
    specificity   : Optional[Dict[str, Callable[[State], int]]] = None,
) -> Decision:
    """Pick the winner and say which paribhāṣā decided it, and over whom.

    ``losers`` holds the rules that genuinely contended — the utsargas an
    apavāda displaced, or the equally specific rivals 1.4.2 had to separate —
    not every candidate the scheduler happened to offer.
    """
    if not candidate_ids:
        raise ValueError("resolve() needs at least one candidate id")
    if len(candidate_ids) == 1:
        return Decision(candidate_ids[0], "sole-candidate", "एकम् एव प्राप्तम्", ())

    key = frozenset(candidate_ids)
    named = next((w for k, w in CONFLICT_OVERRIDES.items() if k <= key and w in candidate_ids), None)   # a named pair inside a larger set
    if named is not None:
        winner = named
        return Decision(winner, "jnapaka", "ज्ञापकः / नामित-अपवादः (docs/AMENDMENT)",
                        tuple(c for c in candidate_ids if c != winner))

    # Ladder 1, step 1 (pāṭha/anuvṛtti): 1.3.2's "upadeśe" — it-saṃjñā and its lopa
    # happen when the affix is *introduced*, so they precede every rule that would
    # otherwise read the affix (7.3.101 must not see the ṅ of ṅas as a yañ).
    it_rules = [c for c in candidate_ids if (1, 3, 2) <= _id_key(c) <= (1, 3, 9)]
    if it_rules:
        winner = min(it_rules, key=_id_key)
        return Decision(winner, "upadesha", paribhasha_layer("upadesha").citation(), ())

    # Art. 21 Ladder 1, step 2 — asiddhatva. Rules inside the tripāḍī cannot see
    # each other's work in descending order (8.2.1), so *para* is not the arbiter:
    # the earlier rule goes first and the later one meets its result afterwards.
    declared_apavada = any(o in candidate_ids for c in candidate_ids for o in (get_sutra(c).apavada_of or ()))
    if all(is_tripadi_sutra(c) for c in candidate_ids):
        if not declared_apavada:
            winner = min(candidate_ids, key=_id_key)
            return Decision(winner, "asiddha", paribhasha_layer("asiddha").citation(), ())
        # an apavāda inside the tripāḍī (8.2.34 over 8.2.31) displaces only the rule it names; the rest keep kram
        gone = {o for c in candidate_ids for o in (get_sutra(c).apavada_of or ()) if o in candidate_ids}
        rest = [c for c in candidate_ids if c not in gone]
        if len(rest) > 1 and all(not (get_sutra(c).apavada_of or ()) or not set(get_sutra(c).apavada_of) & set(rest) for c in rest):
            winner = min(rest, key=_id_key)
            return Decision(winner, "asiddha", paribhasha_layer("asiddha").citation(), tuple(sorted(gone)))

    # Ladder 1, step 3 — pratiṣedha. A prohibition is settled before the rules it forbids contend
    # (the autonomous loop does it in apply_pratishedhas; a pool-driven scanner offers it as a candidate).
    prohibitions = [c for c in candidate_ids if get_sutra(c).sutra_type is SutraType.PRATISHEDHA]
    if prohibitions:
        first = min(prohibitions, key=_id_key)
        return Decision(first, "pratishedha", "प्रतिषेधः — निषेधः प्रथमं निर्णीयते (Art. 21)",
                        tuple(c for c in candidate_ids if c != first))

    # Ladder 1: an apavāda displaces the utsarga *it names* and nothing else
    # ("purastād apavādā anantarān vidhīn bādhante nottarān": a later rule at the same
    # junction — 6.1.102 beside 6.1.97 — is para and still contends).
    displaced: set[str] = set()
    for cid in candidate_ids:
        for other in (get_sutra(cid).apavada_of or ()):
            if other in candidate_ids:
                displaced.add(other)
    if displaced:
        remaining = [c for c in candidate_ids if c not in displaced]
        if len(remaining) == 1:
            return Decision(remaining[0], "apavada",
                            paribhasha_layer("apavada").citation(), tuple(sorted(displaced)))
        pre_losers = tuple(sorted(displaced))
        candidate_ids = remaining
    else:
        pre_losers = ()

    skipped = _skipped_unmodelled()

    vibh = []
    for cid in candidate_ids:
        try:
            rec = get_sutra(cid)
        except Exception:
            continue
        if rec.sutra_type is SutraType.VIBHASHA:
            vibh.append(cid)
    if vibh and len(candidate_ids) > 1:
        winner = min(vibh, key=_id_key)
        return Decision(
            winner, "vikalpa", paribhasha_layer("vikalpa").citation(),
            (),  # do not BLOCK the other branch — it remains a live option
            skipped_unmodelled=skipped,
        )

    proposal = _soi_proposal(candidate_ids, state, specificity)
    para = paribhasha_layer("para")
    winner = max(candidate_ids, key=_id_key)

    # Ladder 1: antaraṅga outranks para (PŚ 38) — only the rules that did not yield.
    info = _zones(candidate_ids, state)
    bahiranga = _bahiranga_losers(candidate_ids, state, info)
    survivors = [c for c in candidate_ids if c not in bahiranga]
    # पूर्व (PŚ 38, the weakest term of the ladder). Two rules *conflict* when applying either leaves the
    # other without a site (विप्रतिषेध): that is *para*'s business (1.4.2, later wins). Rules that leave
    # each other alone do not conflict, and Aṣṭādhyāyī kram (Art. 3) orders them — the earlier goes first. This
    # is how 7.2.79 (s-lopa) comes before 7.3.101 although both are open at once.
    if info and len(survivors) > 1:
        from engine.scheduler import probe

        after = {c: probe(c, state) for c in survivors if c in info}

        def _kills(x: str, y: str) -> bool:
            try:
                return not get_sutra(y).cond(after[x])
            except Exception:
                return False

        def _inserts_only(x: str) -> bool:
            """x only adds varṇas/Terms (an āgama, a doubling): it never rewrites what stands, so it cannot
            tie with another rule over the same letters — Aṣṭādhyāyī kram orders it."""
            a, b = state.terms, after[x].terms
            if len(a) != len(b):
                return True
            for ta, tb in zip(a, b):
                it = iter("".join(v.slp1 for v in tb.varnas))
                if not all(ch in it for ch in "".join(v.slp1 for v in ta.varnas)):
                    return False
            return True

        def _order_matters(x: str, y: str) -> bool:
            """Both rewrite the same Term and the two orders end differently: a real विप्रतिषेध even though
            neither kills the other (7.4.60 vs 7.4.66 on the abhyāsa: sasmāra, not *sarsmāra) — para decides."""
            if not (info[x][0] & info[y][0]) or is_tripadi_sutra(x) != is_tripadi_sutra(y) or _inserts_only(x) or _inserts_only(y):
                return False       # tripāḍī is asiddha to what precedes it (8.2.1): its place is fixed, not para
            try:
                xy, yx = probe(y, after[x]), probe(x, after[y])
                return [_term_sig(t) for t in xy.terms] != [_term_sig(t) for t in yx.terms]
            except Exception:
                return False

        def _defeated(c: str) -> bool:
            if c not in info:
                return False
            return any(
                r != c and r in info and _id_key(r) > _id_key(c)
                and (_kills(c, r) or _kills(r, c) or _order_matters(c, r))
                for r in survivors
            )

        undefeated = [c for c in survivors if c in info and not _defeated(c)]
        first = min(undefeated, key=_id_key) if undefeated else None
        if first is not None and first != max(survivors, key=_id_key):
            return Decision(first, "purva", paribhasha_layer("purva").citation(),
                            tuple(c for c in candidate_ids if c != first) + pre_losers,
                            skipped_unmodelled=skipped)
    if bahiranga and survivors:
        inner = max(survivors, key=_id_key)
        if inner != winner:
            return Decision(
                inner, "antaranga", paribhasha_layer("antaranga").citation(),
                tuple(sorted(bahiranga)) + pre_losers, skipped_unmodelled=skipped,
            )
        winner = inner
    return Decision(
        winner, para.key, para.citation(),
        tuple(c for c in candidate_ids if c != winner) + pre_losers,
        skipped_unmodelled=skipped,
        soi_proposal=proposal if proposal and proposal != winner else None,
    )


def resolve(
    candidate_ids : List[str],
    state         : State,
    specificity   : Optional[Dict[str, Callable[[State], int]]] = None,
) -> str:
    """The winning sūtra id. See :func:`resolve_with_reason` for the why."""
    return resolve_with_reason(candidate_ids, state, specificity).winner


def _default_specificity(rec: SutraRecord) -> int:
    """Diagnostic only — counted fields, never a reason to win."""
    score = 0
    if rec.adhikara_scope != ("", ""):
        score += 1
    if rec.blocks_sutra_ids:
        score += 1
    if rec.atidesha_source:
        score += 1
    if rec.apavada_of:
        score += 2
    return score


def record_decision(state: State, decision: Decision) -> None:
    """Art. 15: a rule that was beaten says who beat it, and by which paribhāṣā.

    Unmodelled-layer contacts and SOI-vs-para disagreements are Art. 18 gaps
    on ``state.meta['art18_gaps']`` — they do not pick a different winner.
    """
    gaps = state.meta.setdefault("art18_gaps", [])
    if decision.skipped_unmodelled and decision.layer == "para":
        gaps.append({
            "kind": "unmodelled_layer",
            "layers": list(decision.skipped_unmodelled),
            "winner": decision.winner,
            "detail": "nitya/antaraṅga not weighed; para (1.4.2) used as floor",
        })
    if decision.soi_proposal:
        gaps.append({
            "kind": "undeclared_apavada_candidate",
            "proposed": decision.soi_proposal,
            "para_winner": decision.winner,
            "detail": "SOI would have picked a different winner; declare apavada_of or an amendment",
        })

    if not decision.losers:
        return
    from engine.trace import make_blocked_step

    form = state.flat_slp1()
    for loser in decision.losers:
        try:
            rec = get_sutra(loser)
        except Exception:
            continue
        state.trace.append(make_blocked_step(
            loser,
            rec.sutra_type.name,
            getattr(rec, "type_label_dev", "") or rec.sutra_type.name,
            form,
            rec.why_dev,
            decision.gate_reason(loser),
        ))
