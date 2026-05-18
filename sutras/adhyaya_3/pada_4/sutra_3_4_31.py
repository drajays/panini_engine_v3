"""
3.4.31  चर्मोदरयोः पूरेः  —  VIDHI

Padaccheda: चर्म-उदरयोः पूरेः

krt-suffix rule: चर्मोदरयोः पूरेः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_31_carmodaray_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "carmodarayoH pUreH",
    text_dev              = "चर्मोदरयोः पूरेः",
    padaccheda_dev        = "चर्म-उदरयोः पूरेः",
    why_dev               = "धातोः प्रत्ययः (३.4.31)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
