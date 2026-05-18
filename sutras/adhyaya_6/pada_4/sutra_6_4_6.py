"""
6.4.6  नृ च  —  VIDHI

Padaccheda: नृ (लुप्तषष्ठ्यन्तनिर्देशः) च

नृ च (6.4.6)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_6_nf_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_6_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nf ca",
    text_dev              = "नृ च",
    padaccheda_dev        = "नृ (लुप्तषष्ठ्यन्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 6.4.6) नृ च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
