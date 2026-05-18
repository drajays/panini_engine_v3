"""
6.3.73  नलोपो नञः  —  VIDHI

Padaccheda: न-लोपः नञः

नलोपो नञः (6.3.73)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_73_nalopo_73"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_73_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nalopo naYaH",
    text_dev              = "नलोपो नञः",
    padaccheda_dev        = "न-लोपः नञः",
    why_dev               = "(सूत्रम् 6.3.73) नलोपो नञः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
