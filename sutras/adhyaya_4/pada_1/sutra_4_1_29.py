"""
4.1.29  नित्यं संज्ञाछन्दसोः  —  VIDHI

Padaccheda: नित्यम् संज्ञा-छन्दसोः

नित्यं संज्ञाछन्दसोः (4.1.29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_29_nityaM_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.29", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityaM saMjYACandasoH",
    text_dev              = "नित्यं संज्ञाछन्दसोः",
    padaccheda_dev        = "नित्यम् संज्ञा-छन्दसोः",
    why_dev               = "(सूत्रम् 4.1.29) नित्यं संज्ञाछन्दसोः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
