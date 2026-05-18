"""
8.1.27  तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः  —  VIDHI

Padaccheda: तिङः गोत्र-आदीनि कुत्सन-आभीक्ष्ण्ययोः

तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः (8.1.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_27_tiNo_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_27_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tiNo gotrAdIni kutsanABIkzRyayoH",
    text_dev              = "तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः",
    padaccheda_dev        = "तिङः गोत्र-आदीनि कुत्सन-आभीक्ष्ण्ययोः",
    why_dev               = "(सूत्रम् 8.1.27) तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
