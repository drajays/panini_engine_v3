"""
2.3.21  इत्थंभूतलक्षणे  —  VIDHI

Padaccheda: इत्थंभूत-लक्षणे (लक्ष्यते अनेनेति लक्षणम्)

Tritiya marks the characteristic in ittham-bhuta context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_21_ittham_laksana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "itTaMBUtalakzaRe",
    text_dev              = "इत्थंभूतलक्षणे",
    padaccheda_dev        = "इत्थंभूत-लक्षणे (लक्ष्यते अनेनेति लक्षणम्)",
    why_dev               = "इत्थंभूत-लक्षणे (२.३.२१)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
