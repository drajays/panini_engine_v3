"""
3.2.8  गापोष्टक्  —  VIDHI

Padaccheda: गा-पोः टक्

krt-suffix rule: गापोष्टक् (8)
Pāṭha: ashtadhyayi.com data.txt row i=32008 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_8_gApozwak_8"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.8", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gApozwak",
    text_dev              = "गापोष्टक्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH gApoH wak kft karmaRi anupasarge supi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः गापोः टक् कृत् कर्मणि अनुपसर्गे सुपि",
    padaccheda_dev        = "गा-पोः टक्",
    why_dev               = "धातोः कृत्-प्रत्ययः [गापोष्टक्] विहितः (३.२.8)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
