"""
3.2.158  स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच्  —  VIDHI

Padaccheda: स्पृहि-गृहि-पति-दयि-निद्रा-तन्द्रा-श्रद्धाभ्यः आलुच्

krt-suffix rule: स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच् (158)
Pāṭha: ashtadhyayi.com data.txt row i=32158 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_158_spfhigfhip_158"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.158", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.158"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.158",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "spfhigfhipatidayinidrAtandrASradDABya Aluc",
    text_dev              = "स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu spfhi-gfhi-pati-dayi-nidrA-tandrA-SradDAByaH Aluc kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु स्पृहि-गृहि-पति-दयि-निद्रा-तन्द्रा-श्रद्धाभ्यः आलुच् कृत्",
    padaccheda_dev        = "स्पृहि-गृहि-पति-दयि-निद्रा-तन्द्रा-श्रद्धाभ्यः आलुच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच्] विहितः (३.२.158)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
