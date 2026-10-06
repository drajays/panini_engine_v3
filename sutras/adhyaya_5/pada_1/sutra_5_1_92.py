"""
5.1.92  सम्परिपूर्वात् ख च  —  VIDHI

Padaccheda: सम्-परि-पूर्वात् ख (लुप्तप्रथमान्तनिर्देशः) च

सम्परिपूर्वात् ख च (5.1.92)
Pāṭha: ashtadhyayi.com data.txt row i=51092 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_92_samparipUr_92"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.92", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.92"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samparipUrvAt Ka ca",
    text_dev              = "सम्परिपूर्वात् ख च",
    samagra_slp1          = "tena nirvfttam taTA tamaDIzwo Bfto BUto BAvI iti sam-pari-pUrvAt vatsarAntAt Candasi CaH KaH ca",
    samagra_dev           = "'तेन निर्वृत्तम्' (तथा) 'तमधीष्टो भृतो भूतो भावी' (इति) सम्-परि-पूर्वात् वत्सरान्तात् छन्दसि छः खः च",
    padaccheda_dev        = "सम्-परि-पूर्वात् ख (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 5.1.92) सम्परिपूर्वात् ख च।",
    anuvritti_from        = ('5.1.78',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
