"""
2.3.26  षष्ठी हेतुप्रयोगे  —  VIDHI

Padaccheda: षष्ठी हेतुप्रयोगे

Sasthi marks hetu when hetu-word is used.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_26_sasthi_hetu"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_26_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zazWI hetuprayoge",
    text_dev              = "षष्ठी हेतुप्रयोगे",
    padaccheda_dev        = "षष्ठी हेतुप्रयोगे",
    why_dev               = "षष्ठी हेतुप्रयोगे (२.३.२६)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
