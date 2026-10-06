"""
3.3.6  किंवृत्ते लिप्सायाम्  —  VIDHI

Padaccheda: किंवृत्ते लिप्सायाम्

krt-suffix rule: किंवृत्ते लिप्सायाम्
Pāṭha: ashtadhyayi.com data.txt row i=33006 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_6_kiMvftte_6"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.6", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kiMvftte lipsAyAm",
    text_dev              = "किंवृत्ते लिप्सायाम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Bavizyati kiMvftte lipsAyAm kft yAvat-purA-nipAtayoH viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भविष्यति किंवृत्ते लिप्सायाम् कृत् यावत्-पुरा-निपातयोः विभाषा",
    padaccheda_dev        = "किंवृत्ते लिप्सायाम्",
    why_dev               = "धातोः प्रत्ययः (३.3.6)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
