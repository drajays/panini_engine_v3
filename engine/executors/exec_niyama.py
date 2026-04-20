"""
engine/executors/exec_niyama.py
─────────────────────────────────

नियम — restricts / narrows a prior vidhi.

May write to state.niyama_gates (signalling that a named vidhi is
narrowed in this context), OR may itself substitute varṇas when the
restriction takes the form of "only this substitute is allowed here".

R1 is NOT exempt when the niyama is acting as a narrowing substitution.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord


def exec_niyama(
    rec  : SutraRecord,
    state: State,
    step : Dict[str, Any],
) -> Tuple[State, bool]:
    if not rec.cond(state):
        return state, False
    new_state = rec.act(state)
    return new_state, True
