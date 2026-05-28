"""
8.2.54  प्रस्त्योऽन्यतरस्याम्  —  VIDHI

Padaccheda: प्रस्त्यः अन्यतरस्याम्

प्रस्त्योऽन्यतरस्याम् (8.2.54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_54_prastyony_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_54_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prastyo'nyatarasyAm",
    text_dev              = "प्रस्त्योऽन्यतरस्याम्",
    padaccheda_dev        = "प्रस्त्यः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.2.54) प्रस्त्योऽन्यतरस्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
