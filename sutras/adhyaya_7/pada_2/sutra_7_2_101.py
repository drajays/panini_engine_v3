"""
7.2.101  जराया जरसन्यतरस्याम्  —  VIDHI

Padaccheda: जराया जरस् अन्यतरस्याम्

जराया जरसन्यतरस्याम् (7.2.101)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_101_jarAyA_101"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_101_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.101"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.101",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jarAyA jarasanyatarasyAm",
    text_dev              = "जराया जरसन्यतरस्याम्",
    padaccheda_dev        = "जराया जरस् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 7.2.101) जराया जरसन्यतरस्याम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
