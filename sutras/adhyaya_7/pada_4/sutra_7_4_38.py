"""
7.4.38  देवसुम्नयोर्यजुषि काठके  —  VIDHI

Padaccheda: देवसुम्नयोः यजुषि काठके

देवसुम्नयोर्यजुषि काठके (7.4.38)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_38_devasumnay_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.38", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "devasumnayoryajuzi kAWake",
    text_dev              = "देवसुम्नयोर्यजुषि काठके",
    padaccheda_dev        = "देवसुम्नयोः यजुषि काठके",
    why_dev               = "(सूत्रम् 7.4.38) देवसुम्नयोर्यजुषि काठके।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
