"""
6.4.15  अनुनासिकस्य क्विझलोः क्ङिति  —  VIDHI

Padaccheda: अनुनासिकस्य क्वि-झलोः क्ङिति

अनुनासिकस्य क्विझलोः क्ङिति (6.4.15)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_15_anunAsikas_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_15_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anunAsikasya kviJaloH kNiti",
    text_dev              = "अनुनासिकस्य क्विझलोः क्ङिति",
    padaccheda_dev        = "अनुनासिकस्य क्वि-झलोः क्ङिति",
    why_dev               = "(सूत्रम् 6.4.15) अनुनासिकस्य क्विझलोः क्ङिति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
