"""
5.1.75  पथः ष्कन्  —  VIDHI

Padaccheda: पथः ष्कन्

पथः ष्कन् (5.1.75)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_75_paTaH_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_75_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paTaH zkan",
    text_dev              = "पथः ष्कन्",
    padaccheda_dev        = "पथः ष्कन्",
    why_dev               = "(सूत्रम् 5.1.75) पथः ष्कन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
