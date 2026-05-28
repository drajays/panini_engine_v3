"""
7.1.86  इतोऽत् सर्वनामस्थाने  —  VIDHI

Padaccheda: इतः अत् सर्वनामस्थाने

इतोऽत् सर्वनामस्थाने (7.1.86)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_86_itot_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.86", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ito't sarvanAmasTAne",
    text_dev              = "इतोऽत् सर्वनामस्थाने",
    padaccheda_dev        = "इतः अत् सर्वनामस्थाने",
    why_dev               = "(सूत्रम् 7.1.86) इतोऽत् सर्वनामस्थाने।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
