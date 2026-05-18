"""
6.4.139  उद ईत्  —  VIDHI

Padaccheda: उदः ईत्

उद ईत् (6.4.139)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_139_uda_139"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_139_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.139"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.139",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uda It",
    text_dev              = "उद ईत्",
    padaccheda_dev        = "उदः ईत्",
    why_dev               = "(सूत्रम् 6.4.139) उद ईत्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
