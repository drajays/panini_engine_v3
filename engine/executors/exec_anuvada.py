"""
engine/executors/exec_anuvada.py
──────────────────────────────────

अनुवाद — pure restatement.  Does nothing.

Purpose: makes inherited anuvṛtti explicit in the trace without
pretending a grammatical operation took place.  The anuvṛtti itself
is ALREADY baked into rec.text_slp1 / text_dev (CONSTITUTION Art. 4),
so execution is truly a no-op.

R1-exempt; the dispatcher records this as APPLIED with form unchanged.
Still returns fired=True so that the trace shows the line.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State
from engine.sutra_type import SutraRecord


def exec_anuvada(
    rec  : SutraRecord,
    state: State,
    step : Dict[str, Any],
) -> Tuple[State, bool]:
    # Most अनुवाद sūtras are unconditional (cond is None).  A few, such as
    # **2.3.46**, carry a *śāstra* gate without phonological effect — honour
    # cond when present so the trace records COND-FALSE instead of a spurious
    # APPLIED row.
    if rec.cond is not None and not rec.cond(state):
        return state, False
    return state, True
