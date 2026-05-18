"""
7.4.76  भृञामित्  —  VIDHI

Padaccheda: भृञाम् इत्

भृञामित् (7.4.76)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_76_BfYAmit_76"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_76_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BfYAmit",
    text_dev              = "भृञामित्",
    padaccheda_dev        = "भृञाम् इत्",
    why_dev               = "(सूत्रम् 7.4.76) भृञामित्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
