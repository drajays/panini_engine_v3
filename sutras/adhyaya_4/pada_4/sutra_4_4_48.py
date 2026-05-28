"""
4.4.48  अण् महिष्यादिभ्यः  —  VIDHI

Padaccheda: अण् महिषी-आदिभ्यः

अण् महिष्यादिभ्यः (4.4.48)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_48_aR_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.48", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aR mahizyAdiByaH",
    text_dev              = "अण् महिष्यादिभ्यः",
    padaccheda_dev        = "अण् महिषी-आदिभ्यः",
    why_dev               = "(सूत्रम् 4.4.48) अण् महिष्यादिभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
