"""
4.1.155  कौसल्यकार्मार्याभ्यां च  —  VIDHI

Padaccheda: कौसल्य-कार्मार्याभ्याम् च

कौसल्यकार्मार्याभ्यां च (4.1.155)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_155_kOsalyakAr_155"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.155", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.155"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.155",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kOsalyakArmAryAByAM ca",
    text_dev              = "कौसल्यकार्मार्याभ्यां च",
    padaccheda_dev        = "कौसल्य-कार्मार्याभ्याम् च",
    why_dev               = "(सूत्रम् 4.1.155) कौसल्यकार्मार्याभ्यां च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
