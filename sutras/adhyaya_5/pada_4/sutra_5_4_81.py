"""
5.4.81  अन्ववतप्ताद्रहसः  —  VIDHI

Padaccheda: अनु-अव-तप्तात् रहसः

अन्ववतप्ताद्रहसः (5.4.81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_81_anvavatapt_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_81_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anvavataptAdrahasaH",
    text_dev              = "अन्ववतप्ताद्रहसः",
    padaccheda_dev        = "अनु-अव-तप्तात् रहसः",
    why_dev               = "(सूत्रम् 5.4.81) अन्ववतप्ताद्रहसः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
