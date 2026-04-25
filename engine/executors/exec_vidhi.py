"""
engine/executors/exec_vidhi.py
────────────────────────────────

विधि — the workhorse.  Performs a phonemic operation on state.terms.

MUST change state.render() when cond(state) is True.
R1 is NOT exempt: the dispatcher raises R1Violation on silent no-op.

The executor itself has no grammatical opinion: it just asks the sūtra
"should I fire?" and, if yes, lets the sūtra's own act() do the edit.
**1.3.9** is special: *cond* false ⇒ still **fired** (vacuous), see ``META_1_3_9_VACUOUS``.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord
from engine.trace      import META_1_3_9_VACUOUS


def exec_vidhi(
    rec  : SutraRecord,
    state: State,
    step : Dict[str, Any],
) -> Tuple[State, bool]:
    if rec.sutra_id == "1.3.9" and not rec.cond(state):
        # Vacuous *prayoga*: **1.3.9** is still “applied” (checked) with *lopa* 0; dispatcher
        # appends *APPLIED_VACUOUS* and skips R1 (see ``engine.dispatcher``).
        state.meta[META_1_3_9_VACUOUS] = True
        return state, True
    if not rec.cond(state):
        return state, False
    new_state = rec.act(state)
    return new_state, True
