"""
3.2.25  हरतेर्दृतिनाथयोः पशौ  —  VIDHI

Padaccheda: हरतेः दृति-नाथयोः पशौ

krt-suffix rule: हरतेर्दृतिनाथयोः पशौ (25)
Pāṭha: ashtadhyayi.com data.txt row i=32025 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_25_haraterdft_25"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.25", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "haraterdftinATayoH paSO",
    text_dev              = "हरतेर्दृतिनाथयोः पशौ",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH harateH dfti-nATayoH paSO kft karmaRi anupasarge supi in",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः हरतेः दृति-नाथयोः पशौ कृत् कर्मणि अनुपसर्गे सुपि इन्",
    padaccheda_dev        = "हरतेः दृति-नाथयोः पशौ",
    why_dev               = "धातोः कृत्-प्रत्ययः [हरतेर्दृतिनाथयोः पशौ] विहितः (३.२.25)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
