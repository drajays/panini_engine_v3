"""
engine/executors/exec_vidhi.py
────────────────────────────────

विधि — the workhorse.  Performs a phonemic operation on state.terms.

MUST change state.render() when cond(state) is True.
R1 is NOT exempt: the dispatcher raises R1Violation on silent no-op.

The executor itself has no grammatical opinion: it just asks the sūtra
"should I fire?" and, if yes, lets the sūtra's own act() do the edit.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord


def exec_vidhi(
    rec  : SutraRecord,
    state: State,
    step : Dict[str, Any],
) -> Tuple[State, bool]:
    if not rec.cond(state):
        return state, False
    new_state = rec.act(state)
    return new_state, True
