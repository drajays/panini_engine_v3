"""
3.2.4  सुपि स्थः  —  VIDHI

Padaccheda: सुपि स्थः

krt-suffix rule: सुपि स्थः (4)
Pāṭha: ashtadhyayi.com data.txt row i=32004 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_4_supi_4"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.4", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "supi sTaH",
    text_dev              = "सुपि स्थः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH supi sTaH kft karmaRi kaH anupasarge",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः सुपि स्थः कृत् कर्मणि कः अनुपसर्गे",
    padaccheda_dev        = "सुपि स्थः",
    why_dev               = "धातोः कृत्-प्रत्ययः [सुपि स्थः] विहितः (३.२.4)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
