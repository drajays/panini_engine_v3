"""
7.4.11  ऋच्छत्यॄताम्  —  VIDHI

Padaccheda: ऋच्छति-ऋ-ॠताम्

ऋच्छत्यॄताम् (7.4.11)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_11_fcCatyFtAm_11"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_11_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fcCatyFtAm",
    text_dev              = "ऋच्छत्यॄताम्",
    padaccheda_dev        = "ऋच्छति-ऋ-ॠताम्",
    why_dev               = "(सूत्रम् 7.4.11) ऋच्छत्यॄताम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
