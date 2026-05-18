"""
6.3.61  इको ह्रस्वोऽङ्यो गालवस्य  —  VIDHI

Padaccheda: इकः ह्रस्वः अङ्यः गालवस्य

इको ह्रस्वोऽङ्यो गालवस्य (6.3.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_61_iko_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iko hrasvo'Nyo gAlavasya",
    text_dev              = "इको ह्रस्वोऽङ्यो गालवस्य",
    padaccheda_dev        = "इकः ह्रस्वः अङ्यः गालवस्य",
    why_dev               = "(सूत्रम् 6.3.61) इको ह्रस्वोऽङ्यो गालवस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
