"""
engine/executors/exec_vibhasha.py
───────────────────────────────────

विभाषा — optional rule.  The dispatcher already consulted the recipe's
vibhasha_choice and declined to reach us if choice == False.  So if we
are here, choice == True and we should apply like a vidhi.

Records the fork in state.vibhasha_forks for audit.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord


def exec_vibhasha(
    rec  : SutraRecord,
    state: State,
    step : Dict[str, Any],
) -> Tuple[State, bool]:
    if not rec.cond(state):
        return state, False

    # Capture the "declined" branch as a fully isolated State before mutating.
    declined_fork = state.fork()
    declined_fork.meta[f"{rec.sutra_id}_skipped_vibhasha"] = True

    new_state = rec.act(state)
    new_state.meta[f"{rec.sutra_id}_applied_vibhasha"] = True
    new_state.vibhasha_forks.append(declined_fork)
    return new_state, True
