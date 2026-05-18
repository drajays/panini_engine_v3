"""
6.4.108  नित्यं करोतेः  —  VIDHI

Padaccheda: नित्यम् करोतेः

नित्यं करोतेः (6.4.108)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_108_nityaM_108"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_108_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityaM karoteH",
    text_dev              = "नित्यं करोतेः",
    padaccheda_dev        = "नित्यम् करोतेः",
    why_dev               = "(सूत्रम् 6.4.108) नित्यं करोतेः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
