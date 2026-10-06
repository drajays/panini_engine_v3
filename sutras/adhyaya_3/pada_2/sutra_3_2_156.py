"""
3.2.156  प्रजोरिनिः  —  VIDHI

Padaccheda: प्र-जोः इनिः

krt-suffix rule: प्रजोरिनिः (156)
Pāṭha: ashtadhyayi.com data.txt row i=32156 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_156_prajoriniH_156"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.156", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.156"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.156",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prajoriniH",
    text_dev              = "प्रजोरिनिः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu prajoH iniH kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु प्रजोः इनिः कृत्",
    padaccheda_dev        = "प्र-जोः इनिः",
    why_dev               = "धातोः कृत्-प्रत्ययः [प्रजोरिनिः] विहितः (३.२.156)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
