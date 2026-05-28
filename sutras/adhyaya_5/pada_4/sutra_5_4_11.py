"""
5.4.11  किमेत्तिङव्ययघादाम्वद्रव्यप्रकर्षे  —  VIDHI

Padaccheda: किम्-एतद्-तिङ्-अव्यय-घात् आमु (लुप्तप्रथमान्तनिर्देशः) अद्रव्यप्रकर्षे

किमेत्तिङव्ययघादाम्वद्रव्यप्रकर्षे (5.4.11)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_11_kimettiNav_11"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.11", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kimettiNavyayaGAdAmvadravyaprakarze",
    text_dev              = "किमेत्तिङव्ययघादाम्वद्रव्यप्रकर्षे",
    padaccheda_dev        = "किम्-एतद्-तिङ्-अव्यय-घात् आमु (लुप्तप्रथमान्तनिर्देशः) अद्रव्यप्रकर्षे",
    why_dev               = "(सूत्रम् 5.4.11) किमेत्तिङव्ययघादाम्वद्रव्यप्रकर्षे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
