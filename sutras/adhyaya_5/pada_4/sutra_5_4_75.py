"""
5.4.75  अच् प्रत्यन्ववपूर्वात् सामलोम्नः  —  VIDHI

Padaccheda: अच् प्रति-अनु-अव-पूर्वात् साम-लोम्नः

अच् प्रत्यन्ववपूर्वात् सामलोम्नः (5.4.75)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_75_ac_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.75", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ac pratyanvavapUrvAt sAmalomnaH",
    text_dev              = "अच् प्रत्यन्ववपूर्वात् सामलोम्नः",
    padaccheda_dev        = "अच् प्रति-अनु-अव-पूर्वात् साम-लोम्नः",
    why_dev               = "(सूत्रम् 5.4.75) अच् प्रत्यन्ववपूर्वात् सामलोम्नः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
