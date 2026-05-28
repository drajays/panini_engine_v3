"""
5.2.13  अद्यश्वीनाऽवष्टब्धे  —  VIDHI

Padaccheda: अद्यश्वीन (लुप्तप्रथमान्तनिर्देशः) अवष्टब्धे

अद्यश्वीनाऽवष्टब्धे (5.2.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_13_adyaSvInA_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.13", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "adyaSvInA'vazwabDe",
    text_dev              = "अद्यश्वीनाऽवष्टब्धे",
    padaccheda_dev        = "अद्यश्वीन (लुप्तप्रथमान्तनिर्देशः) अवष्टब्धे",
    why_dev               = "(सूत्रम् 5.2.13) अद्यश्वीनाऽवष्टब्धे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
