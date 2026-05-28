"""
5.1.121  न नञ्पूर्वात्तत्पुरुषादचतुरसंगतलवणवटयुधकतरसलसेभ्यः  —  VIDHI

Padaccheda: न नञ्-पूर्वात् तत्पुरुषात् अचतुर-संगत-लवण-वट-युध-कत-रस-लसेभ्यः

न नञ्पूर्वात्तत्पुरुषादचतुरसंगतलवणवटयुधकतरसलसेभ्यः (5.1.121)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_121_na_121"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.121", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na naYpUrvAttatpuruzAdacaturasaMgatalavaRavawayuDakatarasalaseByaH",
    text_dev              = "न नञ्पूर्वात्तत्पुरुषादचतुरसंगतलवणवटयुधकतरसलसेभ्यः",
    padaccheda_dev        = "न नञ्-पूर्वात् तत्पुरुषात् अचतुर-संगत-लवण-वट-युध-कत-रस-लसेभ्यः",
    why_dev               = "(सूत्रम् 5.1.121) न नञ्पूर्वात्तत्पुरुषादचतुरसंगतलवणवटयुधकतरसलसेभ्यः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
