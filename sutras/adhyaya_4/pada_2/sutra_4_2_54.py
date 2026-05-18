"""
4.2.54  भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ  —  VIDHI

Padaccheda: भौरिक्य-आदि-ऐषुकार्य-आदिभ्यः विधल्-भक्तलौ

भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ (4.2.54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_54_BOrikyAdyE_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_54_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BOrikyAdyEzukAryAdiByo viDalBaktalO",
    text_dev              = "भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ",
    padaccheda_dev        = "भौरिक्य-आदि-ऐषुकार्य-आदिभ्यः विधल्-भक्तलौ",
    why_dev               = "(सूत्रम् 4.2.54) भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
