"""
7.1.48  इष्ट्वीनमिति च  —  VIDHI

Padaccheda: इष्ट्‍वीनम् इति च

इष्ट्वीनमिति च (7.1.48)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_48_izwvInamit_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_48_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "izwvInamiti ca",
    text_dev              = "इष्ट्वीनमिति च",
    padaccheda_dev        = "इष्ट्‍वीनम् इति च",
    why_dev               = "(सूत्रम् 7.1.48) इष्ट्वीनमिति च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
