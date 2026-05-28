"""
6.1.124  इन्द्रे च  —  VIDHI

Padaccheda: इन्द्रे च (नित्यम् )

इन्द्रे च (6.1.124)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_124_indre_124"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_124_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "indre ca",
    text_dev              = "इन्द्रे च",
    padaccheda_dev        = "इन्द्रे च (नित्यम् )",
    why_dev               = "(सूत्रम् 6.1.124) इन्द्रे च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
