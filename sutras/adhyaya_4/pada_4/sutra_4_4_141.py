"""
4.4.141  नक्षत्राद्घः  —  VIDHI

Padaccheda: नक्षत्रात् घः

नक्षत्राद्घः (4.4.141)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_141_nakzatrAdG_141"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_141_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.141"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.141",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nakzatrAdGaH",
    text_dev              = "नक्षत्राद्घः",
    padaccheda_dev        = "नक्षत्रात् घः",
    why_dev               = "(सूत्रम् 4.4.141) नक्षत्राद्घः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
