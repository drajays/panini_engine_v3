"""
3.2.68  अदोऽनन्ने  —  VIDHI

Padaccheda: अदः अनन्ने

krt-suffix rule: अदोऽनन्ने (68)
Pāṭha: ashtadhyayi.com data.txt row i=32068 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_68_adonanne_68"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.68", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'adonanne',
    text_dev              = 'अदोऽनन्ने',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH adaH ananne kft supi upasarge api viw",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः अदः अनन्ने कृत् सुपि उपसर्गे अपि विट्",
    padaccheda_dev        = "अदः अनन्ने",
    why_dev               = "धातोः कृत्-प्रत्ययः [अदोऽनन्ने] विहितः (३.२.68)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
