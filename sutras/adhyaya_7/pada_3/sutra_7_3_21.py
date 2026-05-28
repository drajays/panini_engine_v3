"""
7.3.21  देवताद्वंद्वे च  —  VIDHI

Padaccheda: देवताद्वन्द्वे च

देवताद्वंद्वे च (7.3.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_21_devatAdvaM_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.21", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "devatAdvaMdve ca",
    text_dev              = "देवताद्वंद्वे च",
    padaccheda_dev        = "देवताद्वन्द्वे च",
    why_dev               = "(सूत्रम् 7.3.21) देवताद्वंद्वे च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
