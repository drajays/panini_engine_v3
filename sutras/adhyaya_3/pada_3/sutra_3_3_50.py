"""
3.3.50  विभाषाऽऽङि रुप्लुवोः  —  VIDHI

Padaccheda: विभाषा आङि रु-प्लुवोः

krt-suffix rule: विभाषाऽऽङि रुप्लुवोः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_50_viBAzANi_50"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_50_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA''Ni rupluvoH",
    text_dev              = "विभाषाऽऽङि रुप्लुवोः",
    padaccheda_dev        = "विभाषा आङि रु-प्लुवोः",
    why_dev               = "धातोः प्रत्ययः (३.3.50)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
