"""
engine/executors/exec_anuvada.py
──────────────────────────────────

अनुवाद — restatement; default *prayoga* is trace-only (no ``act``).

When ``rec.act`` is set, it runs after ``cond`` passes (meta / *śruti*
stamps, arm clears — still typically no *varṇa* tape change).

Purpose: inherited *anuvṛtti* is baked into ``rec.text_slp1`` / ``text_dev``
(CONSTITUTION Art. 4); the trace row records the *śāstra* line.

R1-exempt; the dispatcher records **AUDIT** when the form is unchanged.
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
    if rec.act is not None:
        return rec.act(state), True
    return state, True
