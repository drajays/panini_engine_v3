"""
4.4.10  पर्पादिभ्यः ष्ठन्  —  VIDHI

Padaccheda: पर्पादिभ्यः ष्ठन्

पर्पादिभ्यः ष्ठन् (4.4.10)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_10_parpAdiBya_10"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_10_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parpAdiByaH zWan",
    text_dev              = "पर्पादिभ्यः ष्ठन्",
    padaccheda_dev        = "पर्पादिभ्यः ष्ठन्",
    why_dev               = "(सूत्रम् 4.4.10) पर्पादिभ्यः ष्ठन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
