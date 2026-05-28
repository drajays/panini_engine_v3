"""
8.1.4  नित्यवीप्सयोः  —  VIDHI

Padaccheda: नित्य-वीप्सयोः

नित्यवीप्सयोः (8.1.4)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_4_nityavIpsa_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityavIpsayoH",
    text_dev              = "नित्यवीप्सयोः",
    padaccheda_dev        = "नित्य-वीप्सयोः",
    why_dev               = "(सूत्रम् 8.1.4) नित्यवीप्सयोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
