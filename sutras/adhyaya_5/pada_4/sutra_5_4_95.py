"""
5.4.95  ग्रामकौटाभ्यां च तक्ष्णः  —  VIDHI

Padaccheda: ग्राम-कौटाभ्याम् च तक्ष्णः

ग्रामकौटाभ्यां च तक्ष्णः (5.4.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_95_grAmakOwAB_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.95", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grAmakOwAByAM ca takzRaH",
    text_dev              = "ग्रामकौटाभ्यां च तक्ष्णः",
    padaccheda_dev        = "ग्राम-कौटाभ्याम् च तक्ष्णः",
    why_dev               = "(सूत्रम् 5.4.95) ग्रामकौटाभ्यां च तक्ष्णः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
