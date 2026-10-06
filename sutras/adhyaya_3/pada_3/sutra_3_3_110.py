"""
3.3.110  विभाषाऽऽख्यानपरिप्रश्नयोरिञ् च  —  VIDHI

Padaccheda: विभाषा आख्यान-परिप्रश्नयोः इञ् च

krt-suffix rule: विभाषाऽऽख्यानपरिप्रश्नयोरिञ् च
Pāṭha: ashtadhyayi.com data.txt row i=33110 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_110_viBAzAKy_110"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.110", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'viBAzAKyAnaparipraSnayoriY ca',
    text_dev              = 'विभाषाऽऽख्यानपरिप्रश्नयोरिञ् च',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm striyAm viBAzA AKyAna-paripraSnayoH iY ca kft Rvul",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्त्रियाम् विभाषा आख्यान-परिप्रश्नयोः इञ् च कृत् ण्वुल्",
    padaccheda_dev        = "विभाषा आख्यान-परिप्रश्नयोः इञ् च",
    why_dev               = "धातोः प्रत्ययः (३.3.110)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
