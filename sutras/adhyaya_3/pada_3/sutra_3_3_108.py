"""
3.3.108  रोगाख्यायां ण्वुल् बहुलम्  —  VIDHI

Padaccheda: रोग-आख्यायाम् ण्वुल् बहुलम्

krt-suffix rule: रोगाख्यायां ण्वुल् बहुलम्
Pāṭha: ashtadhyayi.com data.txt row i=33108 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_108_rogAKyAyAM_108"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.108", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rogAKyAyAM Rvul bahulam",
    text_dev              = "रोगाख्यायां ण्वुल् बहुलम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm striyAm rogAKyAyAm Rvul bahulam kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्त्रियाम् रोगाख्यायाम् ण्वुल् बहुलम् कृत्",
    padaccheda_dev        = "रोग-आख्यायाम् ण्वुल् बहुलम्",
    why_dev               = "धातोः प्रत्ययः (३.3.108)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
