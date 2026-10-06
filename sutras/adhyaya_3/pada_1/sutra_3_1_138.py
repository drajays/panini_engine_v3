"""
3.1.138  अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च  —  VIDHI

Padaccheda: अन्-उपसर्गात् लिम्प-विन्द-धारि-पारि-वेदि-उदेजि-चेति-साति-साहिभ्यः च

Krt suffix rule from dhatu: अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च (138)
Pāṭha: ashtadhyayi.com data.txt row i=31138 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_138_anupasargAll_138"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.138", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.138"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anupasargAllimpavindaDAripArivedyudejicetisAtisAhiByaSca",
    text_dev              = "अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH anupasargAt limpa-vinda-DAri-pAri-vedi-udeji-ceti-sAti-sAhiByaH ca kft SaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः अनुपसर्गात् लिम्प-विन्द-धारि-पारि-वेदि-उदेजि-चेति-साति-साहिभ्यः च कृत् शः",
    padaccheda_dev        = "अन्-उपसर्गात् लिम्प-विन्द-धारि-पारि-वेदि-उदेजि-चेति-साति-साहिभ्यः च",
    why_dev               = "धातोः [अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च]-प्रत्ययः विहितः (३.१.138)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
