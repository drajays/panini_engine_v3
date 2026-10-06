"""
3.2.119  अपरोक्षे च  —  VIDHI

Padaccheda: अ-परोक्षे च

krt-suffix rule: अपरोक्षे च (119)
Pāṭha: ashtadhyayi.com data.txt row i=32119 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_119_aparokze_119"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.119", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aparokze ca",
    text_dev              = "अपरोक्षे च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte aparokze ca kft anadyatane sme law",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते अपरोक्षे च कृत् अनद्यतने स्मे लट्",
    padaccheda_dev        = "अ-परोक्षे च",
    why_dev               = "धातोः कृत्-प्रत्ययः [अपरोक्षे च] विहितः (३.२.119)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
