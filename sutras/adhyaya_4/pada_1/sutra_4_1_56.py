"""
4.1.56  न क्रोडादिबह्वचः  —  VIDHI

Padaccheda: न क्रोडा-आदि-बहु-अचः

न क्रोडादिबह्वचः (4.1.56)
Pāṭha: ashtadhyayi.com data.txt row i=41056 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_56_na_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.56", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.56",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na kroqAdibahvacaH",
    text_dev              = "न क्रोडादिबह्वचः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt na kroqa-Adi-bahvacaH NIz sva-aNgAt ca upasarjanAt a-saMyoga-upaDAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् न क्रोड-आदि-बह्वचः ङीष् स्व-अङ्गात् च उपसर्जनात् अ-संयोग-उपधात्",
    padaccheda_dev        = "न क्रोडा-आदि-बहु-अचः",
    why_dev               = "(सूत्रम् 4.1.56) न क्रोडादिबह्वचः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
