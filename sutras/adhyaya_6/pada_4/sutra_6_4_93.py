"""
6.4.93  चिण्णमुलोर्दीर्घोऽन्यतरस्याम्  —  VIDHI

Padaccheda: चिण्-णमुँल्ोः दीर्घः अन्यतरस्याम्

चिण्णमुलोर्दीर्घोऽन्यतरस्याम् (6.4.93)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_93_ciRRamulor_93"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.93", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.93"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ciRRamulordIrGo'nyatarasyAm",
    text_dev              = "चिण्णमुलोर्दीर्घोऽन्यतरस्याम्",
    padaccheda_dev        = "चिण्-णमुँल्ोः दीर्घः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.4.93) चिण्णमुलोर्दीर्घोऽन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
