"""
4.4.103  गुडादिभ्यष्ठञ्  —  VIDHI

Padaccheda: गुड-आदिभ्यः ठञ्

गुडादिभ्यष्ठञ् (4.4.103)
Pāṭha: ashtadhyayi.com data.txt row i=44103 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_103_guqAdiByaz_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.103", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "guqAdiByazWaY",
    text_dev              = "गुडादिभ्यष्ठञ्",
    samagra_slp1          = "tatra sADuH iti guqAdiByaH saMjYAyAm WaY",
    samagra_dev           = "'तत्र साधुः' (इति) गुडादिभ्यः संज्ञायाम् ठञ्",
    padaccheda_dev        = "गुड-आदिभ्यः ठञ्",
    why_dev               = "(सूत्रम् 4.4.103) गुडादिभ्यष्ठञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
