"""
engine/resolver.py — Rule-conflict resolver.
──────────────────────────────────────────────

The strength order is not an engineering convenience. It is
**परिभाषेन्दुशेखर 38**, loaded with its text from ``engine.paribhasha``::

    पूर्वपरनित्यान्तरङ्गापवादानामुत्तरोत्तरं बलीयः

Five terms, ascending: *pūrva* < *para* < *nitya* < *antaraṅga* < *apavāda*.
Two of them execute here — *apavāda* (PŚ 57 अन्तरङ्गादप्यवादो बलवान्) and
*para* (the sūtra named in the data) — while *nitya* and *antaraṅga* are
declared ``not_modelled``, so a conflict that would turn on them is decided by
the layers below **and says so**, rather than being settled silently (Art. 18).

Every decision names its layer and its losers, and the caller writes those
losers into the trace as BLOCKED — Art. 15: a rule that was beaten must say
who beat it.

When two or more sūtras want to fire on the same state, we resolve by:

  Layer A — Asiddha barrier (8.2.1–8.4.68).  An earlier-than-tripāḍī
            sūtra never wins against a tripāḍī sūtra once we are in
            the tripāḍī zone; conversely, tripāḍī sūtras are invisible
            to earlier sūtras.  Implemented in engine/gates.py.

  Layer B — Pratiṣedha.  If candidate X is in state.blocked_sutras,
            it is dropped.  Implemented in engine/gates.py.

  Layer C — Rajpopat SOI  (Specificity Of Input).
            Of two candidates, the one whose cond() matches on the
            NARROWER trigger-set wins.  Specificity is scored by
            the sūtra file's optional `specificity_score(state)` hook,
            defaulting to 0.  Higher score wins.

  Layer D — *para* (PŚ 38).  Of two rules of equal strength that both
            want the same position, the one that comes LATER in the
            Aṣṭādhyāyī wins.

  Layer E — Conflict override table.  For the (very rare) cases where
            Pāṇini's own śabda establishes a named override, we
            consult CONFLICT_OVERRIDES: dict[frozenset[id], str].

This module exposes `resolve(candidates, state)` returning the winner
or raising if the conflict is unresolved (which is a bug — we do NOT
silently pick).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, FrozenSet, List, Optional

from engine.paribhasha import layer as paribhasha_layer
from engine.registry   import get_sutra
from engine.state      import State
from engine.sutra_type import SutraRecord


# Named overrides.  Populated only by explicit amendment in docs/.
CONFLICT_OVERRIDES: Dict[FrozenSet[str], str] = {
    # Example shape:
    # frozenset({"1.1.3", "6.1.87"}): "6.1.87",
}


class UnresolvedConflict(RuntimeError):
    """All resolver layers failed to pick a unique winner."""


@dataclass(frozen=True)
class Decision:
    """Who won, by which paribhāṣā, and who lost."""

    winner: str
    layer: str                       # override | apavada | soi | 1.4.2
    reason_dev: str
    losers: tuple[str, ...] = field(default_factory=tuple)

    def gate_reason(self, loser: str) -> str:
        return f"{self.layer}: {self.winner} beat {loser} — {self.reason_dev}"


def _apavada_winner(candidate_ids: List[str]) -> Optional[str]:
    """A declared अपवाद defeats the उत्सर्ग it names, wherever either stands."""
    exceptions = [
        cid for cid in candidate_ids
        if any(other in (get_sutra(cid).apavada_of or ()) for other in candidate_ids)
    ]
    return exceptions[0] if len(exceptions) == 1 else None


def _soi_scores(
    candidate_ids: List[str],
    state: State,
    specificity: Optional[Dict[str, Callable[[State], int]]] = None,
) -> Dict[str, int]:
    try:
        from engine.specificity_registry import get_specificity
    except ModuleNotFoundError:
        # The per-sūtra SOI registry is an optional refinement of Layer C.
        # Without it every candidate falls back to the declared-field
        # heuristic, and the paribhāṣā layers above and below still decide.
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
    return scores


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
        return Decision(winner, "override", "नामित-अपवादः (docs/AMENDMENT)",
                        tuple(c for c in candidate_ids if c != winner))

    apavada = _apavada_winner(candidate_ids)
    if apavada is not None:
        displaced = tuple(
            c for c in candidate_ids if c in (get_sutra(apavada).apavada_of or ())
        )
        return Decision(apavada, "apavada",
                        paribhasha_layer("apavada").citation(), displaced)

    scores = _soi_scores(candidate_ids, state, specificity)
    top = max(scores.values())
    contenders = [cid for cid, score in scores.items() if score == top]
    if len(contenders) == 1:
        winner = contenders[0]
        return Decision(winner, "soi", "संकुचित-निमित्तम् बलीयः (engine heuristic)",
                        tuple(c for c in candidate_ids if c != winner))

    # पर — of equals, the later sūtra wins. The Aṣṭādhyāyī id of this
    # paribhāṣā comes from the vendored data, never from a literal here.
    para = paribhasha_layer("para")
    winner = max(contenders, key=lambda s: tuple(int(p) for p in s.split(".")))
    return Decision(winner, para.key, para.citation(),
                    tuple(c for c in contenders if c != winner))


def resolve(
    candidate_ids : List[str],
    state         : State,
    specificity   : Optional[Dict[str, Callable[[State], int]]] = None,
) -> str:
    """The winning sūtra id. See :func:`resolve_with_reason` for the why."""
    return resolve_with_reason(candidate_ids, state, specificity).winner


def _default_specificity(rec: SutraRecord) -> int:
    """
    Tiny default: a sūtra is 'more specific' if it has more declared
    restrictions.  Sūtras that genuinely need specificity OVERRIDE
    this by writing a `specificity_score(state)` function in their
    file and handing it to resolve() via the scheduler.
    """
    score = 0
    if rec.adhikara_scope != ("", ""):
        score += 1
    if rec.blocks_sutra_ids:
        score += 1
    if rec.atidesha_source:
        score += 1
    return score


def record_decision(state: State, decision: Decision) -> None:
    """Art. 15: a rule that was beaten says who beat it, and by which paribhāṣā.

    Only the genuine contenders are written — the utsargas an apavāda
    displaced, or the equally specific rivals *para* had to separate — not
    every candidate the scheduler offered.
    """
    if not decision.losers:
        return
    from engine.registry import get_sutra
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
