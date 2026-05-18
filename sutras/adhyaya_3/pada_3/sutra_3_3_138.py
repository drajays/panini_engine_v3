"""
3.3.138  परस्मिन् विभाषा  —  VIDHI

Padaccheda: परस्मिन् विभाषा

krt-suffix rule: परस्मिन् विभाषा
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_138_parasmin_138"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_138_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.138"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parasmin viBAzA",
    text_dev              = "परस्मिन् विभाषा",
    padaccheda_dev        = "परस्मिन् विभाषा",
    why_dev               = "धातोः प्रत्ययः (३.3.138)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
