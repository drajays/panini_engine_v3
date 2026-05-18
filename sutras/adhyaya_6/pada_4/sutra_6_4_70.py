"""
6.4.70  मयतेरिदन्यतरस्याम्  —  VIDHI

Padaccheda: मयतेः इत् अन्यतरस्याम्

मयतेरिदन्यतरस्याम् (6.4.70)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_70_mayaterida_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_70_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mayateridanyatarasyAm",
    text_dev              = "मयतेरिदन्यतरस्याम्",
    padaccheda_dev        = "मयतेः इत् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.4.70) मयतेरिदन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
