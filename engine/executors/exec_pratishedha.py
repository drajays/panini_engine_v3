"""
engine/executors/exec_pratishedha.py
──────────────────────────────────────

प्रतिषेध — blocks named sūtras from firing.

Two shapes:

  1. Static block:
         blocks_sutra_ids=("7.3.102",)  with no cond/act.
     → unconditionally adds 7.3.102 to state.blocked_sutras.

  2. Conditional block:
         cond(state) returns True iff block applies; act(state) adds
         the correct IDs to state.blocked_sutras.

R1-exempt.  Form never changes.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord


def exec_pratishedha(
    rec  : SutraRecord,
    state: State,
    step : Dict[str, Any],
) -> Tuple[State, bool]:
    if rec.cond is not None and not rec.cond(state):
        return state, False

    new_state = state
    if rec.act is not None:
        new_state = rec.act(state)

    # Always add the statically-declared blocks as well (if any).
    for blocked in rec.blocks_sutra_ids:
        new_state.blocked_sutras.add(blocked)
    return new_state, True
