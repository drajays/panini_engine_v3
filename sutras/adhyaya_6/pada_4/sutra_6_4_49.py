"""
6.4.49  यस्य हलः  —  VIDHI

Padaccheda: यस्य हलः

यस्य हलः (6.4.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_49_yasya_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_49_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yasya halaH",
    text_dev              = "यस्य हलः",
    padaccheda_dev        = "यस्य हलः",
    why_dev               = "(सूत्रम् 6.4.49) यस्य हलः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
