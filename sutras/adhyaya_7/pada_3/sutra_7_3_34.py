"""
7.3.34  नोदात्तोपदेशस्य मान्तस्यानाचमेः  —  VIDHI

Padaccheda: न उपदिष्ट&उदात्तस्य /seq=1 <BV>&()म&()अन्तस्य अन्-आचमेः

नोदात्तोपदेशस्य मान्तस्यानाचमेः (7.3.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_34_nodAttopad_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_34_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nodAttopadeSasya mAntasyAnAcameH",
    text_dev              = "नोदात्तोपदेशस्य मान्तस्यानाचमेः",
    padaccheda_dev        = "न उपदिष्ट&उदात्तस्य /seq=1 <BV>&()म&()अन्तस्य अन्-आचमेः",
    why_dev               = "(सूत्रम् 7.3.34) नोदात्तोपदेशस्य मान्तस्यानाचमेः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
