"""
6.1.176  ह्रस्वनुड्भ्यां मतुप्  —  VIDHI

Padaccheda: ह्रस्व-नुड्-भ्याम् मतुप्

ह्रस्वनुड्भ्यां मतुप् (6.1.176)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_176_hrasvanuqB_176"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_176_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.176"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.176",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hrasvanuqByAM matup",
    text_dev              = "ह्रस्वनुड्भ्यां मतुप्",
    padaccheda_dev        = "ह्रस्व-नुड्-भ्याम् मतुप्",
    why_dev               = "(सूत्रम् 6.1.176) ह्रस्वनुड्भ्यां मतुप्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
