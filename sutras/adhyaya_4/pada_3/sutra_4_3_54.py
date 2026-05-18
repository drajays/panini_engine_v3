"""
4.3.54  दिगादिभ्यो यत्  —  VIDHI

Padaccheda: दिक्-आदिभ्यः यत्

दिगादिभ्यो यत् (4.3.54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_54_digAdiByo_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_54_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "digAdiByo yat",
    text_dev              = "दिगादिभ्यो यत्",
    padaccheda_dev        = "दिक्-आदिभ्यः यत्",
    why_dev               = "(सूत्रम् 4.3.54) दिगादिभ्यो यत्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
