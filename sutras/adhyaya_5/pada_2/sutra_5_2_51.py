"""
5.2.51  षट्कतिकतिपयचतुरां थुक्  —  VIDHI

Padaccheda: षट्-कति-कतिपय-चतुराम् थुक्

षट्कतिकतिपयचतुरां थुक् (5.2.51)
Pāṭha: ashtadhyayi.com data.txt row i=52051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_51_zawkatikat_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.51", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zawkatikatipayacaturAM Tuk",
    text_dev              = "षट्कतिकतिपयचतुरां थुक्",
    samagra_slp1          = "tasya pUraRe iti qawi zaw-kati-katipaya-caturAm Tuk",
    samagra_dev           = "'तस्य पूरणे' (इति) डटि षट्-कति-कतिपय-चतुराम् थुक्",
    padaccheda_dev        = "षट्-कति-कतिपय-चतुराम् थुक्",
    why_dev               = "(सूत्रम् 5.2.51) षट्कतिकतिपयचतुरां थुक्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
