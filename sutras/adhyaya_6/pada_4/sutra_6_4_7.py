"""
6.4.7  नोपधायाः  —  VIDHI

Padaccheda: न (लुप्तषष्ठ्यन्तनिर्देशः) उपधायाः

नोपधायाः (6.4.7)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_7_nopaDAyAH_7"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_7_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nopaDAyAH",
    text_dev              = "नोपधायाः",
    padaccheda_dev        = "न (लुप्तषष्ठ्यन्तनिर्देशः) उपधायाः",
    why_dev               = "(सूत्रम् 6.4.7) नोपधायाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
