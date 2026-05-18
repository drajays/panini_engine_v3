"""
6.2.19  न भूवाक्चिद्दिधिषु  —  VIDHI

Padaccheda: न भू-वाक्-चित्-दिधिषु

न भूवाक्चिद्दिधिषु (6.2.19)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_19_na_19"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_19_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na BUvAkciddiDizu",
    text_dev              = "न भूवाक्चिद्दिधिषु",
    padaccheda_dev        = "न भू-वाक्-चित्-दिधिषु",
    why_dev               = "(सूत्रम् 6.2.19) न भूवाक्चिद्दिधिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
