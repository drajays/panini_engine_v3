"""
3.2.3  आतोऽनुपसर्गे कः  —  VIDHI

Padaccheda: आतः अन्-उपसर्गे कः

krt-suffix rule: आतोऽनुपसर्गे कः (3)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_3_Atonupasa_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_3_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ato'nupasarge kaH",
    text_dev              = "आतोऽनुपसर्गे कः",
    padaccheda_dev        = "आतः अन्-उपसर्गे कः",
    why_dev               = "धातोः कृत्-प्रत्ययः [आतोऽनुपसर्गे कः] विहितः (३.२.3)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
