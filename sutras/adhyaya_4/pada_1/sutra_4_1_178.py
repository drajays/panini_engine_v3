"""
4.1.178  न प्राच्यभर्गादियौधेयादिभ्यः  —  VIDHI

Padaccheda: न प्राच्य-भर्ग-आदि-यौधेय-आदिभ्यः

न प्राच्यभर्गादियौधेयादिभ्यः (4.1.178)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_178_na_178"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_178_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.178"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.178",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na prAcyaBargAdiyODeyAdiByaH",
    text_dev              = "न प्राच्यभर्गादियौधेयादिभ्यः",
    padaccheda_dev        = "न प्राच्य-भर्ग-आदि-यौधेय-आदिभ्यः",
    why_dev               = "(सूत्रम् 4.1.178) न प्राच्यभर्गादियौधेयादिभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
