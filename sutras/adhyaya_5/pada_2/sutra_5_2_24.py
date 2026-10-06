"""
5.2.24  तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ  —  VIDHI

Padaccheda: तस्य पाकमूले पीलु-आदि-कर्ण-आदिभ्यः कुणप्-जाहचौ

तस्य पाकमूले पील्वदिकर्णादिभ्यः कुणब्जाहचौ (5.2.24)
Pāṭha: ashtadhyayi.com data.txt row i=52024 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_24_tasya_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.24", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'tasya pAkamUle pIlvAdikarRAdiByaH kuRabjAhacO',
    text_dev              = 'तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ',
    samagra_slp1          = "tasya pAka-mUle iti pIlvAdi-karRAdiByaH kuRap-jAhacO",
    samagra_dev           = "'तस्य पाक-मूले' (इति) पील्वादि-कर्णादिभ्यः कुणप्-जाहचौ",
    padaccheda_dev        = "तस्य पाकमूले पीलु-आदि-कर्ण-आदिभ्यः कुणप्-जाहचौ",
    why_dev               = "(सूत्रम् 5.2.24) तस्य पाकमूले पील्वदिकर्णादिभ्यः कुणब्जाहचौ।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
