"""
engine/executors/exec_nipatana.py
───────────────────────────────────

निपातन — stamps an exceptional form, freezes further vidhis.

Replaces the last term's varṇas with the nipātana sequence,
and sets state.nipatana_flag = True.  Subsequent VIDHI/NIYAMA
steps will be frozen out by the dispatcher's gate.

The sūtra file may provide its own act() for fancier nipātanas
(e.g. replacing only part of a term).  Default behaviour: replace
state.terms[-1].varnas with varṇas built from rec.nipatana_form_slp1.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

from engine.state      import State, Varna
from engine.sutra_type import SutraRecord


def _varnas_from_slp1(slp1: str) -> list:
    # Zero-opinion converter: used only as a DEFAULT when the sūtra file
    # did not override act().  Real sūtras should build Varnas with both
    # slp1 and dev set via phonology/varna.py's mk() helper.
    from phonology.varna import mk
    return [mk(ch) for ch in slp1]


def exec_nipatana(
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
        if not new_state.terms:
            return new_state, False
        tail = new_state.terms[-1]
        tail.varnas = _varnas_from_slp1(rec.nipatana_form_slp1 or "")

    new_state.nipatana_flag = True
    return new_state, True
