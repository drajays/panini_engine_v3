"""
6.2.28  पूगेष्वन्यतरस्याम्  —  VIDHI

Padaccheda: पूगेषु अन्यतरस्याम्

पूगेष्वन्यतरस्याम् (6.2.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_28_pUgezvanya_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_28_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUgezvanyatarasyAm",
    text_dev              = "पूगेष्वन्यतरस्याम्",
    padaccheda_dev        = "पूगेषु अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.2.28) पूगेष्वन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
