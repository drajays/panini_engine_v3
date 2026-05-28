"""
7.3.22  नेन्द्रस्य परस्य  —  VIDHI

Padaccheda: न इन्द्रस्य परस्य

नेन्द्रस्य परस्य (7.3.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_22_nendrasya_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.22", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_3_22_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nendrasya parasya",
    text_dev              = "नेन्द्रस्य परस्य",
    padaccheda_dev        = "न इन्द्रस्य परस्य",
    why_dev               = "(सूत्रम् 7.3.22) नेन्द्रस्य परस्य।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
