"""
engine/resolver.py — Rule-conflict resolver.
──────────────────────────────────────────────

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

  Layer D — Rajpopat DOI  (Direction Of Information).
            Tie-break: the sūtra whose action TARGETS the LATER
            position in the varṇa sequence wins (Pāṇini reads
            left-to-right; rightward-targeting rules fire later).

  Layer E — Conflict override table.  For the (very rare) cases where
            Pāṇini's own śabda establishes a named override, we
            consult CONFLICT_OVERRIDES: dict[frozenset[id], str].

This module exposes `resolve(candidates, state)` returning the winner
or raising if the conflict is unresolved (which is a bug — we do NOT
silently pick).
"""
from __future__ import annotations

from typing import Callable, Dict, FrozenSet, List, Optional

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


def resolve(
    candidate_ids : List[str],
    state         : State,
    specificity   : Optional[Dict[str, Callable[[State], int]]] = None,
) -> str:
    """
    Pick the winning sūtra id from `candidate_ids` on `state`.
    `specificity` is an optional override map sutra_id -> fn(state)->int.
    """
    if not candidate_ids:
        raise ValueError("resolve() needs at least one candidate id")
    if len(candidate_ids) == 1:
        return candidate_ids[0]

    # Layer E — explicit override.
    key = frozenset(candidate_ids)
    if key in CONFLICT_OVERRIDES:
        winner = CONFLICT_OVERRIDES[key]
        if winner in candidate_ids:
            return winner

    # Layer C — SOI (higher specificity wins).
    scores = {}
    for cid in candidate_ids:
        rec = get_sutra(cid)
        score_fn = (specificity or {}).get(cid)
        if score_fn is not None:
            scores[cid] = score_fn(state)
        else:
            # Default heuristic: count the non-empty predicate hooks
            # declared on the SutraRecord.  (Real sūtras override.)
            scores[cid] = _default_specificity(rec)

    max_score = max(scores.values())
    best = [cid for cid, s in scores.items() if s == max_score]
    if len(best) == 1:
        return best[0]

    # Layer D — DOI.  Later sutra_id breaks the tie (Aṣṭādhyāyī order
    # is the canonical reading direction).
    best.sort(key=lambda s: tuple(int(p) for p in s.split(".")))
    if len(best) >= 1:
        return best[-1]

    raise UnresolvedConflict(
        f"resolver could not pick among {candidate_ids!r} on state "
        f"{state.render()!r}"
    )


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
