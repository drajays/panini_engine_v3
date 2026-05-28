"""
4.4.26  व्यञ्जनैरुपसिक्ते  —  VIDHI

Padaccheda: व्यञ्जनैः उपसिक्ते

व्यञ्जनैरुपसिक्ते (4.4.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_26_vyaYjanEru_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.26", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyaYjanErupasikte",
    text_dev              = "व्यञ्जनैरुपसिक्ते",
    padaccheda_dev        = "व्यञ्जनैः उपसिक्ते",
    why_dev               = "(सूत्रम् 4.4.26) व्यञ्जनैरुपसिक्ते।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
