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

    # Record the fork BEFORE mutating so 'alternative' reflects the
    # form had we declined the option.
    alternative_form = state.render()
    new_state = rec.act(state)
    new_state.vibhasha_forks.append({
        "sutra_id"    : rec.sutra_id,
        "choice_made" : True,
        "alternative" : alternative_form,
    })
    return new_state, True
