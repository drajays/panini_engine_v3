"""
3.2.146  निन्दहिंसक्लिशखादविनाशपरिक्षिपपरिरटपरिवादिव्याभाषासूञो वुञ्  —  VIDHI

Padaccheda: निन्द-हिंस-क्लिश-खाद-विनाश-परिक्षिप-परिरट-परिवादि-व्याभाष-असूयः (पञ्चम्यर्थे प्रथमा) वुञ्

krt-suffix rule: निन्दहिंसक्लिशखादविनाशपरिक्षिपपरिरटपरिवादिव्याभाषासूञो वुञ् (146)
Pāṭha: ashtadhyayi.com data.txt row i=32146 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_146_nindahiMsa_146"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.146", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.146"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.146",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nindahiMsakliSaKAdavinASaparikzipaparirawaparivAdivyABAzAsUYo vuY",
    text_dev              = "निन्दहिंसक्लिशखादविनाशपरिक्षिपपरिरटपरिवादिव्याभाषासूञो वुञ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu ninda-hiMsa-kliSa-KAda-vinASa-parikzipa-parirawa-parivAdi-vyABAza-asUyaH vuY kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु निन्द-हिंस-क्लिश-खाद-विनाश-परिक्षिप-परिरट-परिवादि-व्याभाष-असूयः वुञ् कृत्",
    padaccheda_dev        = "निन्द-हिंस-क्लिश-खाद-विनाश-परिक्षिप-परिरट-परिवादि-व्याभाष-असूयः (पञ्चम्यर्थे प्रथमा) वुञ्",
    why_dev               = "धातोः कृत्-प्रत्ययः [निन्दहिंसक्लिशखादविनाशपरिक्षिपपरिरटपरिवादिव्याभाषासूञो वुञ्] विहितः (३.२.146)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
