"""
4.4.104  पथ्यतिथिवसतिस्वपतेर्ढञ्  —  VIDHI

Padaccheda: पथि-अतिथि-वसति-स्वपतेः ढञ्

पथ्यतिथिवसतिस्वपतेर्ढञ् (4.4.104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_104_paTyatiTiv_104"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_104_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paTyatiTivasatisvapaterQaY",
    text_dev              = "पथ्यतिथिवसतिस्वपतेर्ढञ्",
    padaccheda_dev        = "पथि-अतिथि-वसति-स्वपतेः ढञ्",
    why_dev               = "(सूत्रम् 4.4.104) पथ्यतिथिवसतिस्वपतेर्ढञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
