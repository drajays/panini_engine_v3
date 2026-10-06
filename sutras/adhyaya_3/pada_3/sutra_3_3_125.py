"""
3.3.125  खनो घ च  —  VIDHI

Padaccheda: खनः घ (लुप्तप्रथमान्तनिर्देशः) च

krt-suffix rule: खनो घ च
Pāṭha: ashtadhyayi.com data.txt row i=33125 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_125_Kano_125"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.125", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Kano Ga ca",
    text_dev              = "खनो घ च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH karaRADikaraRayoH KanaH Ga ca kft karaRa-aDikaraRayoH puMsi GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः करणाधिकरणयोः खनः घ च कृत् करण-अधिकरणयोः पुंसि घञ्",
    padaccheda_dev        = "खनः घ (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "धातोः प्रत्ययः (३.3.125)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
