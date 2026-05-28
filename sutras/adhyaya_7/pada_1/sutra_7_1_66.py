"""
7.1.66  उपात् प्रशंसायाम्  —  VIDHI

Padaccheda: उपात् प्रशंसायाम्

उपात् प्रशंसायाम् (7.1.66)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_66_upAt_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.66", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upAt praSaMsAyAm",
    text_dev              = "उपात् प्रशंसायाम्",
    padaccheda_dev        = "उपात् प्रशंसायाम्",
    why_dev               = "(सूत्रम् 7.1.66) उपात् प्रशंसायाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
