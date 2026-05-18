"""
7.3.9  पदान्तस्यान्यतरस्याम्  —  VIDHI

Padaccheda: पदान्तस्य अन्यतरस्याम्

पदान्तस्यान्यतरस्याम् (7.3.9)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_9_padAntasyA_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_9_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "padAntasyAnyatarasyAm",
    text_dev              = "पदान्तस्यान्यतरस्याम्",
    padaccheda_dev        = "पदान्तस्य अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 7.3.9) पदान्तस्यान्यतरस्याम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
