"""
4.3.136  बिल्वादिभ्योऽण्  —  VIDHI

Padaccheda: बिल्व-आदिभ्यः अण्

बिल्वादिभ्योऽण् (4.3.136)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_136_bilvAdiByo_136"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_136_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.136"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.136",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bilvAdiByo'R",
    text_dev              = "बिल्वादिभ्योऽण्",
    padaccheda_dev        = "बिल्व-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 4.3.136) बिल्वादिभ्योऽण्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
