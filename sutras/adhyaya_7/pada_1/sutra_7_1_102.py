"""
7.1.102  उदोष्ठ्यपूर्वस्य  —  VIDHI

Padaccheda: उत् ओष्ठ्यपूर्वस्य

उदोष्ठ्यपूर्वस्य (7.1.102)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_102_udozWyapUr_102"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.102", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.102"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.102",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udozWyapUrvasya",
    text_dev              = "उदोष्ठ्यपूर्वस्य",
    padaccheda_dev        = "उत् ओष्ठ्यपूर्वस्य",
    why_dev               = "(सूत्रम् 7.1.102) उदोष्ठ्यपूर्वस्य।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
