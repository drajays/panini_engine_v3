"""
6.2.87  प्रस्थेऽवृद्धमकर्क्यादीनाम्  —  VIDHI

Padaccheda: प्रस्थे अ-वृद्धम् अ-कर्क्की-आदीनाम्

प्रस्थेऽवृद्धमकर्क्यादीनाम् (6.2.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_87_prasTevfd_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prasTe'vfdDamakarkyAdInAm",
    text_dev              = "प्रस्थेऽवृद्धमकर्क्यादीनाम्",
    padaccheda_dev        = "प्रस्थे अ-वृद्धम् अ-कर्क्की-आदीनाम्",
    why_dev               = "(सूत्रम् 6.2.87) प्रस्थेऽवृद्धमकर्क्यादीनाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
