"""
4.1.178  न प्राच्यभर्गादियौधेयादिभ्यः  —  VIDHI

Padaccheda: न प्राच्य-भर्ग-आदि-यौधेय-आदिभ्यः

न प्राच्यभर्गादियौधेयादिभ्यः (4.1.178)
Pāṭha: ashtadhyayi.com data.txt row i=41178 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_178_na_178"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.178", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.178"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.178",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na prAcyaBargAdiyODeyAdiByaH",
    text_dev              = "न प्राच्यभर्गादियौधेयादिभ्यः",
    samagra_slp1          = "prAcya-BargAdi-yODeyAdiByaH striyAm tadrAjasya luk na",
    samagra_dev           = "प्राच्य-भर्गादि-यौधेयादिभ्यः स्त्रियाम्  तद्राजस्य लुक् न",
    padaccheda_dev        = "न प्राच्य-भर्ग-आदि-यौधेय-आदिभ्यः",
    why_dev               = "(सूत्रम् 4.1.178) न प्राच्यभर्गादियौधेयादिभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
