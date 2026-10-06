"""
5.2.138  कंशंभ्यां बभयुस्तितुतयसः  —  VIDHI

Padaccheda: कं-शंभ्याम् ब-भ-युस्-ति-तु-त-यसः

कंशंभ्यां बभयुस्तितुतयसः (5.2.138)
Pāṭha: ashtadhyayi.com data.txt row i=52138 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_138_kaMSaMByAM_138"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.138", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.138"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaMSaMByAM baBayustitutayasaH",
    text_dev              = "कंशंभ्यां बभयुस्तितुतयसः",
    samagra_slp1          = "tat asya asmin astIti iti kam-SaMByAm ba-Ba-yus-ti-tu-ta-yasaH",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) कम्-शंभ्याम् ब-भ-युस्-ति-तु-त-यसः",
    padaccheda_dev        = "कं-शंभ्याम् ब-भ-युस्-ति-तु-त-यसः",
    why_dev               = "(सूत्रम् 5.2.138) कंशंभ्यां बभयुस्तितुतयसः।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
