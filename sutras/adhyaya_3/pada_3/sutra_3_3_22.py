"""
3.3.22  उपसर्गे रुवः  —  VIDHI

Padaccheda: उपसर्गे रुवः

krt-suffix rule: उपसर्गे रुवः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_22_upasarge_22"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.22", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasarge ruvaH",
    text_dev              = "उपसर्गे रुवः",
    padaccheda_dev        = "उपसर्गे रुवः",
    why_dev               = "धातोः प्रत्ययः (३.3.22)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
