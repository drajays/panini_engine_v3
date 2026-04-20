"""
engine/executors/exec_samjna.py
─────────────────────────────────

संज्ञा — registers a technical term.

Executor contract (CONSTITUTION Art. 1, contract table SUTRA_TYPE_CONTRACTS[SAMJNA]):
  • MUST NOT touch state.terms / varṇas.
  • MUST write to state.samjna_registry when cond(state) is True
    and act(state) runs.
  • R1-exempt: form_before == form_after is CORRECT.
  • R2 catches SAMJNA that fires without registry mutation.

Shape of a SAMJNA sūtra file's cond/act:
    def cond(state): ...           # returns bool
    def act(state): ...             # returns MUTATED state (same object)
                                    # — the clone was made by the dispatcher
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord


def exec_samjna(
    rec  : SutraRecord,
    state: State,
    step : Dict[str, Any],
) -> Tuple[State, bool]:
    if not rec.cond(state):
        return state, False
    new_state = rec.act(state)
    return new_state, True
