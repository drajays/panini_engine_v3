"""
7.2.2  अतो र्लान्तस्य  —  VIDHI

Padaccheda: अतः ल (लुप्तषष्ठ्यन्तनिर्देशः) अन्तस्य

अतो र्लान्तस्य (7.2.2)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_2_ato_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_2_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ato rlAntasya",
    text_dev              = "अतो र्लान्तस्य",
    padaccheda_dev        = "अतः ल (लुप्तषष्ठ्यन्तनिर्देशः) अन्तस्य",
    why_dev               = "(सूत्रम् 7.2.2) अतो र्लान्तस्य।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
