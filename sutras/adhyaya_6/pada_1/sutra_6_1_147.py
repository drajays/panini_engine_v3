"""
6.1.147  आश्चर्यमनित्ये  —  VIDHI

Padaccheda: आश्चर्यम् अनित्ये

आश्चर्यमनित्ये (6.1.147)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_147_AScaryaman_147"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_147_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.147"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.147",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AScaryamanitye",
    text_dev              = "आश्चर्यमनित्ये",
    padaccheda_dev        = "आश्चर्यम् अनित्ये",
    why_dev               = "(सूत्रम् 6.1.147) आश्चर्यमनित्ये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
