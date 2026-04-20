"""
engine/executors/exec_adhikara.py
───────────────────────────────────

अधिकार — pushes a scope entry onto state.adhikara_stack.

The stack entry is a dict:
    { "id": rec.sutra_id, "scope_end": rec.adhikara_scope[1], "text_dev": ... }

If the sūtra file provides a custom act(), we honour it (e.g. to also
set state.tripadi_zone = True on 8.2.1).  Otherwise we just push.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord


def exec_adhikara(
    rec  : SutraRecord,
    state: State,
    step : Dict[str, Any],
) -> Tuple[State, bool]:
    if rec.cond is not None and not rec.cond(state):
        return state, False

    if rec.act is not None:
        new_state = rec.act(state)
    else:
        new_state = state
        new_state.adhikara_stack.append({
            "id"        : rec.sutra_id,
            "scope_end" : rec.adhikara_scope[1],
            "text_dev"  : rec.text_dev,
        })
    return new_state, True
