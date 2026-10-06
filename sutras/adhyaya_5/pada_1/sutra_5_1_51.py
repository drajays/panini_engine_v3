"""
5.1.51  वस्नद्रव्याभ्यां ठन्कनौ  —  VIDHI

Padaccheda: वस्न-द्रव्याभ्याम् ठन्-कनौ

वस्नद्रव्याभ्यां ठन्कनौ (5.1.51)
Pāṭha: ashtadhyayi.com data.txt row i=51051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_51_vasnadravy_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.51", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vasnadravyAByAM WankanO",
    text_dev              = "वस्नद्रव्याभ्यां ठन्कनौ",
    samagra_slp1          = "tad harati vahati Avahati iti vasna-dravyAByAm Wan-kanO",
    samagra_dev           = "'तद् हरति, वहति, आवहति' (इति) वस्न-द्रव्याभ्याम् ठन्-कनौ",
    padaccheda_dev        = "वस्न-द्रव्याभ्याम् ठन्-कनौ",
    why_dev               = "(सूत्रम् 5.1.51) वस्नद्रव्याभ्यां ठन्कनौ।",
    anuvritti_from        = ('5.1.19',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
