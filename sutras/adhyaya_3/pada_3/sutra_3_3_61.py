"""
3.3.61  व्यधजपोरनुपसर्गे  —  VIDHI

Padaccheda: व्यध-जपोः अन्-उपसर्गे

krt-suffix rule: व्यधजपोरनुपसर्गे
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_61_vyaDajapor_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyaDajaporanupasarge",
    text_dev              = "व्यधजपोरनुपसर्गे",
    padaccheda_dev        = "व्यध-जपोः अन्-उपसर्गे",
    why_dev               = "धातोः प्रत्ययः (३.3.61)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
