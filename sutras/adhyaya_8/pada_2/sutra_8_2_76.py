"""
8.2.76  र्वोरुपधाया दीर्घ इकः  —  VIDHI

Padaccheda: ऋ-वोः उपधाया दीर्घ इकः

र्वोरुपधाया दीर्घ इकः (8.2.76)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_76_rvorupaDAy_76"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rvorupaDAyA dIrGa ikaH",
    text_dev              = "र्वोरुपधाया दीर्घ इकः",
    padaccheda_dev        = "ऋ-वोः उपधाया दीर्घ इकः",
    why_dev               = "(सूत्रम् 8.2.76) र्वोरुपधाया दीर्घ इकः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
