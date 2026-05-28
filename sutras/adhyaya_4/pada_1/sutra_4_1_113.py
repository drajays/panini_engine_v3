"""
4.1.113  अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः  —  VIDHI

Padaccheda: अ-वृद्धाभ्यः नदी-मानुषीभ्यः तत्-नामिकाभ्यः

अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः (4.1.113)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_113_avfdDAByo_113"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.113", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.113"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.113",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avfdDAByo nadImAnuzIByastannAmikAByaH",
    text_dev              = "अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः",
    padaccheda_dev        = "अ-वृद्धाभ्यः नदी-मानुषीभ्यः तत्-नामिकाभ्यः",
    why_dev               = "(सूत्रम् 4.1.113) अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
