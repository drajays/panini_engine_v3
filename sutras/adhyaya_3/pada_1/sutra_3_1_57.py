"""
3.1.57  इरितो वा  —  VIDHI

Padaccheda: इरितः वा

Krt suffix rule from dhatu: इरितो वा (57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_57_irito_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_57_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "irito vA",
    text_dev              = "इरितो वा",
    padaccheda_dev        = "इरितः वा",
    why_dev               = "धातोः [इरितो वा]-प्रत्ययः विहितः (३.१.57)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
