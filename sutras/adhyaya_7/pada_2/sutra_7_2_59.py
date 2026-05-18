"""
7.2.59  न वृद्भ्यश्चतुर्भ्यः  —  VIDHI

Padaccheda: न वृद्‍भ्यः चतुर्भ्यः

न वृद्भ्यश्चतुर्भ्यः (7.2.59)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_59_na_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_59_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na vfdByaScaturByaH",
    text_dev              = "न वृद्भ्यश्चतुर्भ्यः",
    padaccheda_dev        = "न वृद्‍भ्यः चतुर्भ्यः",
    why_dev               = "(सूत्रम् 7.2.59) न वृद्भ्यश्चतुर्भ्यः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
