"""
7.3.94  यङो वा  —  VIDHI

Padaccheda: यङः वा

यङो वा (7.3.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_94_yaNo_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaNo vA",
    text_dev              = "यङो वा",
    padaccheda_dev        = "यङः वा",
    why_dev               = "(सूत्रम् 7.3.94) यङो वा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
