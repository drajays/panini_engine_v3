"""
8.1.31  नह प्रत्यारम्भे  —  VIDHI

Padaccheda: नह प्रत्यारम्भे

नह प्रत्यारम्भे (8.1.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_31_naha_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naha pratyAramBe",
    text_dev              = "नह प्रत्यारम्भे",
    padaccheda_dev        = "नह प्रत्यारम्भे",
    why_dev               = "(सूत्रम् 8.1.31) नह प्रत्यारम्भे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
