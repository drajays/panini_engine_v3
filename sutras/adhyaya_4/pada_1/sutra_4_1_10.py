"""
4.1.10  न षट्स्वस्रादिभ्यः  —  VIDHI

Padaccheda: न षट्-स्वस्रादिभ्यः

न षट्स्वस्रादिभ्यः (4.1.10)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_10_na_10"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_10_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na zawsvasrAdiByaH",
    text_dev              = "न षट्स्वस्रादिभ्यः",
    padaccheda_dev        = "न षट्-स्वस्रादिभ्यः",
    why_dev               = "(सूत्रम् 4.1.10) न षट्स्वस्रादिभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
