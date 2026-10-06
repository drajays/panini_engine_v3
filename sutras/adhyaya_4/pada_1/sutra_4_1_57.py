"""
4.1.57  सहनञ्विद्यमानपूर्वाच्च  —  VIDHI

Padaccheda: सह-नञ्-विद्यमान-पूर्वात् च

सहनञ्विद्यमानपूर्वाच्च (4.1.57)
Pāṭha: ashtadhyayi.com data.txt row i=41057 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_57_sahanaYvid_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.57", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sahanaYvidyamAnapUrvAcca",
    text_dev              = "सहनञ्विद्यमानपूर्वाच्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt saha-naY-vidyamAna-pUrvAt ca NIz sva-aNgAt upasarjanAt a-saMyoga-upaDAt na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् सह-नञ्-विद्यमान-पूर्वात् च ङीष् स्व-अङ्गात् उपसर्जनात् अ-संयोग-उपधात् न",
    padaccheda_dev        = "सह-नञ्-विद्यमान-पूर्वात् च",
    why_dev               = "(सूत्रम् 4.1.57) सहनञ्विद्यमानपूर्वाच्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
