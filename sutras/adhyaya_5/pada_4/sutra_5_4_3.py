"""
5.4.3  स्थूलादिभ्यः प्रकारवचने कन्  —  VIDHI

Padaccheda: स्थूल-आदिभ्यः प्रकारवचने कन्

स्थूलादिभ्यः प्रकारवचने कन् (5.4.3)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_3_sTUlAdiBya_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_3_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTUlAdiByaH prakAravacane kan",
    text_dev              = "स्थूलादिभ्यः प्रकारवचने कन्",
    padaccheda_dev        = "स्थूल-आदिभ्यः प्रकारवचने कन्",
    why_dev               = "(सूत्रम् 5.4.3) स्थूलादिभ्यः प्रकारवचने कन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
