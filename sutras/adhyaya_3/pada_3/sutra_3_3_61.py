"""
3.3.61  व्यधजपोरनुपसर्गे  —  VIDHI

Padaccheda: व्यध-जपोः अन्-उपसर्गे

krt-suffix rule: व्यधजपोरनुपसर्गे
Pāṭha: ashtadhyayi.com data.txt row i=33061 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_61_vyaDajapor_61"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.61", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyaDajaporanupasarge",
    text_dev              = "व्यधजपोरनुपसर्गे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm vyaDa-japoH anupasarge kft ap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् व्यध-जपोः अनुपसर्गे कृत् अप्",
    padaccheda_dev        = "व्यध-जपोः अन्-उपसर्गे",
    why_dev               = "धातोः प्रत्ययः (३.3.61)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
