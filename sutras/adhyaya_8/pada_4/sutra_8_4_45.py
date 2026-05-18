"""
8.4.45  यरोऽनुनासिकेऽनुनासिको वा  —  VIDHI

Padaccheda: यरः अनुनासिके अनुनासिकः वा

यरोऽनुनासिकेऽनुनासिको वा (8.4.45)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_45_yaronunAs_45"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_45_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaro'nunAsike'nunAsiko vA",
    text_dev              = "यरोऽनुनासिकेऽनुनासिको वा",
    padaccheda_dev        = "यरः अनुनासिके अनुनासिकः वा",
    why_dev               = "(सूत्रम् 8.4.45) यरोऽनुनासिकेऽनुनासिको वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
