"""
3.3.49  उदि श्रयतियौतिपूद्रुवः  —  VIDHI

Padaccheda: उदि श्रयति-यौति-पू-द्रुवः

krt-suffix rule: उदि श्रयतियौतिपूद्रुवः
Pāṭha: ashtadhyayi.com data.txt row i=33049 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_49_udi_49"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.49", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udi SrayatiyOtipUdruvaH",
    text_dev              = "उदि श्रयतियौतिपूद्रुवः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm udi Srayati-yOti-pU-druvaH kft GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् उदि श्रयति-यौति-पू-द्रुवः कृत् घञ्",
    padaccheda_dev        = "उदि श्रयति-यौति-पू-द्रुवः",
    why_dev               = "धातोः प्रत्ययः (३.3.49)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
