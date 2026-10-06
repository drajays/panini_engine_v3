"""
3.3.37  परिन्योर्नीणोर्द्यूताभ्रेषयोः  —  VIDHI

Padaccheda: परि-न्योः नी-इणोः द्यूत-अभ्रेषयोः

krt-suffix rule: परिन्योर्नीणोर्द्यूताभ्रेषयोः
Pāṭha: ashtadhyayi.com data.txt row i=33037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_37_parinyornI_37"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.37", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parinyornIRordyUtABrezayoH",
    text_dev              = "परिन्योर्नीणोर्द्यूताभ्रेषयोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm pari-nyoH nI-RoH dyuta-aBrezayoH kft GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् परि-न्योः नी-णोः द्युत-अभ्रेषयोः कृत् घञ्",
    padaccheda_dev        = "परि-न्योः नी-इणोः द्यूत-अभ्रेषयोः",
    why_dev               = "धातोः प्रत्ययः (३.3.37)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
