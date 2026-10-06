"""
3.2.49  आशिषि हनः  —  VIDHI

Padaccheda: आशिषि हनः

krt-suffix rule: आशिषि हनः (49)
Pāṭha: ashtadhyayi.com data.txt row i=32049 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_49_ASizi_49"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.49", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASizi hanaH",
    text_dev              = "आशिषि हनः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH ASizi hanaH kft karmaRi anupasarge supi qaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः आशिषि हनः कृत् कर्मणि अनुपसर्गे सुपि डः",
    padaccheda_dev        = "आशिषि हनः",
    why_dev               = "धातोः कृत्-प्रत्ययः [आशिषि हनः] विहितः (३.२.49)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
