"""
4.2.3  नक्षत्रेण युक्तः कालः  —  VIDHI

Padaccheda: नक्षत्रेण युक्तः कालः

नक्षत्रेण युक्तः कालः (4.2.3)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_3_nakzatreRa_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_3_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nakzatreRa yuktaH kAlaH",
    text_dev              = "नक्षत्रेण युक्तः कालः",
    padaccheda_dev        = "नक्षत्रेण युक्तः कालः",
    why_dev               = "(सूत्रम् 4.2.3) नक्षत्रेण युक्तः कालः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
