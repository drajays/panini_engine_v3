"""
4.4.111  पाथोनदीभ्यां ड्यण्  —  VIDHI

Padaccheda: पाथो-नदीभ्याम् ड्यण्

पाथोनदीभ्यां ड्यण् (4.4.111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_111_pATonadIBy_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_111_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pATonadIByAM qyaR",
    text_dev              = "पाथोनदीभ्यां ड्यण्",
    padaccheda_dev        = "पाथो-नदीभ्याम् ड्यण्",
    why_dev               = "(सूत्रम् 4.4.111) पाथोनदीभ्यां ड्यण्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
