"""
5.2.5  सर्वचर्मणः कृतः खखञौ  —  VIDHI

Padaccheda: सर्वचर्मणः कृतः ख-खञौ

सर्वचर्मणः कृतः खखञौ (5.2.5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_5_sarvacarma_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_5_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sarvacarmaRaH kftaH KaKaYO",
    text_dev              = "सर्वचर्मणः कृतः खखञौ",
    padaccheda_dev        = "सर्वचर्मणः कृतः ख-खञौ",
    why_dev               = "(सूत्रम् 5.2.5) सर्वचर्मणः कृतः खखञौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
