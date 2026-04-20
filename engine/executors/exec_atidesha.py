"""
engine/executors/exec_atidesha.py
───────────────────────────────────

अतिदेश — extends a property X from A to B by analogy.

MUST write to state.atidesha_map[(source, dest)] = target_property.
MUST NOT change state.terms directly.  The vidhi that later USES the
atideśa is what will mutate varṇas.

If a sūtra provides an explicit act(), we call it; otherwise we
install (source,dest)->target from the record fields.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord


def exec_atidesha(
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
        new_state.atidesha_map[(rec.atidesha_source, rec.atidesha_dest)] \
            = rec.atidesha_target
    return new_state, True
