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
}

# Decision.layer values Art. 21 permits. Constitutional test greps this set.
DECISION_LAYERS: FrozenSet[str] = frozenset({
    "sole-candidate",
    "override",
    "jnapaka",
    "upadesha",
    "asiddha",
    "apavada",
    "vikalpa",
    "para",
})


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
    if key in CONFLICT_OVERRIDES and CONFLICT_OVERRIDES[key] in candidate_ids:
        winner = CONFLICT_OVERRIDES[key]
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
    if all(is_tripadi_sutra(c) for c in candidate_ids):
        winner = min(candidate_ids, key=_id_key)
        return Decision(winner, "asiddha", paribhasha_layer("asiddha").citation(), ())

    apavada = _apavada_winner(candidate_ids)
    if apavada is not None:
        displaced = tuple(
            c for c in candidate_ids if c in (get_sutra(apavada).apavada_of or ())
        )
        return Decision(apavada, "apavada",
                        paribhasha_layer("apavada").citation(), displaced)

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
    return Decision(
        winner, para.key, para.citation(),
        tuple(c for c in candidate_ids if c != winner),
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
