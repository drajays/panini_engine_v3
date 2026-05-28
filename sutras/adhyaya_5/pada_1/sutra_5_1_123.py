"""
5.1.123  वर्णदृढादिभ्यः ष्यञ् च  —  VIDHI

Padaccheda: वर्ण-दृढ-आदिभ्यः ष्यञ् च

वर्णदृढादिभ्यः ष्यञ् च (5.1.123)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_123_varRadfQAd_123"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.123", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.123"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varRadfQAdiByaH zyaY ca",
    text_dev              = "वर्णदृढादिभ्यः ष्यञ् च",
    padaccheda_dev        = "वर्ण-दृढ-आदिभ्यः ष्यञ् च",
    why_dev               = "(सूत्रम् 5.1.123) वर्णदृढादिभ्यः ष्यञ् च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
