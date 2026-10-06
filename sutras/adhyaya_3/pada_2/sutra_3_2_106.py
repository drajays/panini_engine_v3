"""
3.2.106  लिटः कानज्वा  —  VIDHI

Padaccheda: लिटः कानच् वा

krt-suffix rule: लिटः कानज्वा (106)
Pāṭha: ashtadhyayi.com data.txt row i=32106 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_106_liwaH_106"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.106", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.106"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.106",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "liwaH kAnajvA",
    text_dev              = "लिटः कानज्वा",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte liwaH kAnac vA kft Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते लिटः कानच् वा कृत् छन्दसि",
    padaccheda_dev        = "लिटः कानच् वा",
    why_dev               = "धातोः कृत्-प्रत्ययः [लिटः कानज्वा] विहितः (३.२.106)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
