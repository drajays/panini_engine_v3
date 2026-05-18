"""
3.4.70  तयोरेव कृत्यक्तखलर्थाः  —  VIDHI

Padaccheda: तयोः एव कृत्य-क्त-खल्-अर्थाः

krt-suffix rule: तयोरेव कृत्यक्तखलर्थाः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_70_tayoreva_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_70_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tayoreva kftyaktaKalarTAH",
    text_dev              = "तयोरेव कृत्यक्तखलर्थाः",
    padaccheda_dev        = "तयोः एव कृत्य-क्त-खल्-अर्थाः",
    why_dev               = "धातोः प्रत्ययः (३.4.70)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
