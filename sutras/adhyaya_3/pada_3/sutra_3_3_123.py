"""
3.3.123  उदङ्कोऽनुदके  —  VIDHI

Padaccheda: उदङ्कः अनुदके

krt-suffix rule: उदङ्कोऽनुदके
Pāṭha: ashtadhyayi.com data.txt row i=33123 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_123_udaNkonud_123"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.123", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.123"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'udaNkonudake',
    text_dev              = 'उदङ्कोऽनुदके',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH karaRADikaraRayoH udaNkaH anudake kft karaRa-aDikaraRayoH ca puMsi GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः करणाधिकरणयोः उदङ्कः अनुदके कृत् करण-अधिकरणयोः च पुंसि घञ्",
    padaccheda_dev        = "उदङ्कः अनुदके",
    why_dev               = "धातोः प्रत्ययः (३.3.123)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
