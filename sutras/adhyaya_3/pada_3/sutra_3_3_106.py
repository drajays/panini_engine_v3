"""
3.3.106  आतश्चोपसर्गे  —  VIDHI

Padaccheda: आतः च उपसर्गे

krt-suffix rule: आतश्चोपसर्गे
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_106_AtaScopasa_106"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_106_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.106"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.106",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtaScopasarge",
    text_dev              = "आतश्चोपसर्गे",
    padaccheda_dev        = "आतः च उपसर्गे",
    why_dev               = "धातोः प्रत्ययः (३.3.106)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
