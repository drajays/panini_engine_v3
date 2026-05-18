"""
7.3.14  प्राचां ग्रामनगराणाम्  —  VIDHI

Padaccheda: प्राचाम् ग्राम-नगराणाम्

प्राचां ग्रामनगराणाम् (7.3.14)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_14_prAcAM_14"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_14_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAcAM grAmanagarARAm",
    text_dev              = "प्राचां ग्रामनगराणाम्",
    padaccheda_dev        = "प्राचाम् ग्राम-नगराणाम्",
    why_dev               = "(सूत्रम् 7.3.14) प्राचां ग्रामनगराणाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
