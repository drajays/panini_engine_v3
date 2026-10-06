"""
3.2.51  कुमारशीर्षयोर्णिनिः  —  VIDHI

Padaccheda: कुमार-शीर्षयोः णिनिः

krt-suffix rule: कुमारशीर्षयोर्णिनिः (51)
Pāṭha: ashtadhyayi.com data.txt row i=32051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_51_kumAraSIrz_51"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.51", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kumAraSIrzayorRiniH",
    text_dev              = "कुमारशीर्षयोर्णिनिः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kumAra-SIrzayoH RiniH kft karmaRi anupasarge supi hanaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कुमार-शीर्षयोः णिनिः कृत् कर्मणि अनुपसर्गे सुपि हनः",
    padaccheda_dev        = "कुमार-शीर्षयोः णिनिः",
    why_dev               = "धातोः कृत्-प्रत्ययः [कुमारशीर्षयोर्णिनिः] विहितः (३.२.51)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
