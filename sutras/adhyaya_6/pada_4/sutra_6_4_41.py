"""
6.4.41  विड्वनोरनुनासिकस्यात्  —  VIDHI

Padaccheda: विट्-वनोः अनुनासिकस्य आत्

विड्वनोरनुनासिकस्यात् (6.4.41)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_41_viqvanoran_41"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_41_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viqvanoranunAsikasyAt",
    text_dev              = "विड्वनोरनुनासिकस्यात्",
    padaccheda_dev        = "विट्-वनोः अनुनासिकस्य आत्",
    why_dev               = "(सूत्रम् 6.4.41) विड्वनोरनुनासिकस्यात्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
