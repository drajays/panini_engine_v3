"""
3.4.17  सृपितृदोः कसुन्  —  VIDHI

Padaccheda: सृपि-तृदोः कसुन्

krt-suffix rule: सृपितृदोः कसुन्
Pāṭha: ashtadhyayi.com data.txt row i=34017 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_17_sfpitfdoH_17"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.17", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sfpitfdoH kasun",
    text_dev              = "सृपितृदोः कसुन्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH sfpi-tfdoH kasun kft Candasi BAvalakzaRe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः सृपि-तृदोः कसुन् कृत् छन्दसि भावलक्षणे",
    padaccheda_dev        = "सृपि-तृदोः कसुन्",
    why_dev               = "धातोः प्रत्ययः (३.4.17)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
