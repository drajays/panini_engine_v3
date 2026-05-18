"""
8.3.54  इडाया वा  —  VIDHI

Padaccheda: इडायाः वा

इडाया वा (8.3.54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_54_iqAyA_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_54_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iqAyA vA",
    text_dev              = "इडाया वा",
    padaccheda_dev        = "इडायाः वा",
    why_dev               = "(सूत्रम् 8.3.54) इडाया वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
