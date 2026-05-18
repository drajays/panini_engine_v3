"""
5.1.105  ऋतोरण्  —  VIDHI

Padaccheda: ऋतोः अण्

ऋतोरण् (5.1.105)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_105_ftoraR_105"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_105_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ftoraR",
    text_dev              = "ऋतोरण्",
    padaccheda_dev        = "ऋतोः अण्",
    why_dev               = "(सूत्रम् 5.1.105) ऋतोरण्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
