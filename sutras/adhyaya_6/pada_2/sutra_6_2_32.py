"""
6.2.32  सप्तमी सिद्धशुष्कपक्वबन्धेष्वकालात्  —  VIDHI

Padaccheda: सप्तमी सिद्ध-शुष्क-पक्व-बन्धेषु अकालात्

सप्तमी सिद्धशुष्कपक्वबन्धेष्वकालात् (6.2.32)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_32_saptamI_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_32_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saptamI sidDaSuzkapakvabanDezvakAlAt",
    text_dev              = "सप्तमी सिद्धशुष्कपक्वबन्धेष्वकालात्",
    padaccheda_dev        = "सप्तमी सिद्ध-शुष्क-पक्व-बन्धेषु अकालात्",
    why_dev               = "(सूत्रम् 6.2.32) सप्तमी सिद्धशुष्कपक्वबन्धेष्वकालात्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
