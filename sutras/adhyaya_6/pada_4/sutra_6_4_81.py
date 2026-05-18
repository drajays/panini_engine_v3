"""
6.4.81  इणो यण्  —  VIDHI

Padaccheda: इणः यण्

इणो यण् (6.4.81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_81_iRo_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_81_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iRo yaR",
    text_dev              = "इणो यण्",
    padaccheda_dev        = "इणः यण्",
    why_dev               = "(सूत्रम् 6.4.81) इणो यण्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
