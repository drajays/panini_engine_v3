"""
3.3.42  संघे चानौत्तराधर्ये  —  VIDHI

Padaccheda: संघे च अनौत्तराधर्ये

krt-suffix rule: संघे चानौत्तराधर्ये
Pāṭha: ashtadhyayi.com data.txt row i=33042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_42_saMGe_42"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.42", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMGe cAnOttarADarye",
    text_dev              = "संघे चानौत्तराधर्ये",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm saMGe ca anOttarADarye kft GaY ceH AdeH kaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् संघे च अनौत्तराधर्ये कृत् घञ् चेः आदेः कः",
    padaccheda_dev        = "संघे च अनौत्तराधर्ये",
    why_dev               = "धातोः प्रत्ययः (३.3.42)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
