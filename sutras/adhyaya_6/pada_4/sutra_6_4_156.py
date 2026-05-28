"""
6.4.156  स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः  —  VIDHI

Padaccheda: स्थूल-दूर-युव-ह्रस्व-क्षिप्र-क्षुद्राणाम् यण्-आदि-परम् पूर्वस्य च गुणः

स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः (6.4.156)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_156_sTUladUray_156"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.156", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.156"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.156",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTUladUrayuvahrasvakziprakzudrARAM yaRAdiparaM pUrvasya ca guRaH",
    text_dev              = "स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः",
    padaccheda_dev        = "स्थूल-दूर-युव-ह्रस्व-क्षिप्र-क्षुद्राणाम् यण्-आदि-परम् पूर्वस्य च गुणः",
    why_dev               = "(सूत्रम् 6.4.156) स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
