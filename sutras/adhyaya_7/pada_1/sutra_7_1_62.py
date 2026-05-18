"""
7.1.62  नेट्यलिटि रधेः  —  VIDHI

Padaccheda: न इटि अ-लिटि रधेः

नेट्यलिटि रधेः (7.1.62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_62_newyaliwi_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_62_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "newyaliwi raDeH",
    text_dev              = "नेट्यलिटि रधेः",
    padaccheda_dev        = "न इटि अ-लिटि रधेः",
    why_dev               = "(सूत्रम् 7.1.62) नेट्यलिटि रधेः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
