"""
3.3.20  परिमाणाख्यायां सर्वेभ्यः  —  VIDHI

Padaccheda: परिमाण-आख्यायाम् सर्वेभ्यः

krt-suffix rule: परिमाणाख्यायां सर्वेभ्यः
Pāṭha: ashtadhyayi.com data.txt row i=33020 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_20_parimARAKy_20"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.20", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parimARAKyAyAM sarveByaH",
    text_dev              = "परिमाणाख्यायां सर्वेभ्यः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm parimARAKyAyAm sarveByaH kft GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् परिमाणाख्यायाम् सर्वेभ्यः कृत् घञ्",
    padaccheda_dev        = "परिमाण-आख्यायाम् सर्वेभ्यः",
    why_dev               = "धातोः प्रत्ययः (३.3.20)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
