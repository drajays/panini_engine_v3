"""
engine/executors/exec_paribhasha.py
─────────────────────────────────────

परिभाषा — sets an interpretive gate that later sūtras read.

MUST write to state.paribhasha_gates.
MUST NOT touch state.terms.
R1-exempt; R3 catches PARIBHASHA that fires without gate change.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord


def exec_paribhasha(
    rec  : SutraRecord,
    state: State,
    step : Dict[str, Any],
) -> Tuple[State, bool]:
    if not rec.cond(state):
        return state, False
    new_state = rec.act(state)
    return new_state, True
