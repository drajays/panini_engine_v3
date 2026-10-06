"""
4.4.42  प्रतिपथमेति ठंश्च  —  VIDHI

Padaccheda: प्रतिपथम् एति (क्रियापदम्) ठन् च

प्रतिपथमेति ठंश्च (4.4.42)
Pāṭha: ashtadhyayi.com data.txt row i=44042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_42_pratipaTam_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.42", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratipaTameti WaMSca",
    text_dev              = "प्रतिपथमेति ठंश्च",
    samagra_slp1          = "tat pratipaTam eti iti samarTAnAm praTamaH Wak Wan ca pratyayaH",
    samagra_dev           = "'तत् प्रतिपथम् एति' (इति) समर्थानाम् प्रथमः ठक् ठन् च प्रत्ययः",
    padaccheda_dev        = "प्रतिपथम् एति (क्रियापदम्) ठन् च",
    why_dev               = "(सूत्रम् 4.4.42) प्रतिपथमेति ठंश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
