"""
6.2.174  ह्रस्वान्तेऽन्त्यात् पूर्वम्  —  VIDHI

Padaccheda: ह्रस्व-अन्ते अन्त्यात् पूर्वम्

ह्रस्वान्तेऽन्त्यात् पूर्वम् (6.2.174)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_174_hrasvAnte_174"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.174"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.174",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hrasvAnte'ntyAt pUrvam",
    text_dev              = "ह्रस्वान्तेऽन्त्यात् पूर्वम्",
    padaccheda_dev        = "ह्रस्व-अन्ते अन्त्यात् पूर्वम्",
    why_dev               = "(सूत्रम् 6.2.174) ह्रस्वान्तेऽन्त्यात् पूर्वम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
