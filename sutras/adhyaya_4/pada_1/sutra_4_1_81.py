"""
4.1.81  दैवयज्ञिशौचिवृक्षिसात्यमुग्रिकाण्ठेविद्धिभ्योऽन्यतरस्याम्  —  VIDHI

Padaccheda: दैवयज्ञि-शौचिवृक्षि-सात्यमुग्रि-काण्ठेविद्धिभ्यः अन्यतरस्याम्

दैवयज्ञिशौचिवृक्षिसात्यमुग्रिकाण्ठेविद्धिभ्योऽन्यतरस्याम् (4.1.81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_81_dEvayajYiS_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_81_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dEvayajYiSOcivfkzisAtyamugrikARWevidDiByo'nyatarasyAm",
    text_dev              = "दैवयज्ञिशौचिवृक्षिसात्यमुग्रिकाण्ठेविद्धिभ्योऽन्यतरस्याम्",
    padaccheda_dev        = "दैवयज्ञि-शौचिवृक्षि-सात्यमुग्रि-काण्ठेविद्धिभ्यः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 4.1.81) दैवयज्ञिशौचिवृक्षिसात्यमुग्रिकाण्ठेविद्धिभ्योऽन्यतरस्याम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
