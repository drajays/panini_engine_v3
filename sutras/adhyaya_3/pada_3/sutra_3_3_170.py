"""
3.3.170  आवश्यकाधमर्ण्ययोर्णिनिः  —  VIDHI

Padaccheda: आवश्यक-आधमर्ण्ययोः णिनिः

krt-suffix rule: आवश्यकाधमर्ण्ययोर्णिनिः
Pāṭha: ashtadhyayi.com data.txt row i=33170 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_170_AvaSyakADa_170"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.170", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.170"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.170",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AvaSyakADamarRyayorRiniH",
    text_dev              = "आवश्यकाधमर्ण्ययोर्णिनिः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH AvaSyaka-ADamarRyayoH RiniH kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः आवश्यक-आधमर्ण्ययोः णिनिः कृत्",
    padaccheda_dev        = "आवश्यक-आधमर्ण्ययोः णिनिः",
    why_dev               = "धातोः प्रत्ययः (३.3.170)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
