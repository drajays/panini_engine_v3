"""
8.3.10  नॄन् पे  —  VIDHI

Padaccheda: नॄन् (लुप्तषष्ठ्यन्तनिर्देशः) पे

नॄन् पे (8.3.10)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_10_nFn_10"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_10_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nFn pe",
    text_dev              = "नॄन् पे",
    padaccheda_dev        = "नॄन् (लुप्तषष्ठ्यन्तनिर्देशः) पे",
    why_dev               = "(सूत्रम् 8.3.10) नॄन् पे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
