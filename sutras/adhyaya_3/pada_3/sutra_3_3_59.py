"""
3.3.59  उपसर्गेऽदः  —  VIDHI

Padaccheda: उपसर्गे अदः

krt-suffix rule: उपसर्गेऽदः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_59_upasarged_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasarge'daH",
    text_dev              = "उपसर्गेऽदः",
    padaccheda_dev        = "उपसर्गे अदः",
    why_dev               = "धातोः प्रत्ययः (३.3.59)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
