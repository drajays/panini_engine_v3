"""
3.2.27  छन्दसि वनसनरक्षिमथाम्  —  VIDHI

Padaccheda: छन्दसि वन-सन-रक्षि-मथाम्

krt-suffix rule: छन्दसि वनसनरक्षिमथाम् (27)
Pāṭha: ashtadhyayi.com data.txt row i=32027 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_27_Candasi_27"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.27", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candasi vanasanarakzimaTAm",
    text_dev              = "छन्दसि वनसनरक्षिमथाम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Candasi vana-sana-rakzi-maTAm kft karmaRi anupasarge supi in",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः छन्दसि वन-सन-रक्षि-मथाम् कृत् कर्मणि अनुपसर्गे सुपि इन्",
    padaccheda_dev        = "छन्दसि वन-सन-रक्षि-मथाम्",
    why_dev               = "धातोः कृत्-प्रत्ययः [छन्दसि वनसनरक्षिमथाम्] विहितः (३.२.27)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
