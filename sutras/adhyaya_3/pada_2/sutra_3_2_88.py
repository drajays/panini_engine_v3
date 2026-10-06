"""
3.2.88  बहुलं छन्दसि  —  VIDHI

Padaccheda: बहुलम् छन्दसि

krt-suffix rule: बहुलं छन्दसि (88)
Pāṭha: ashtadhyayi.com data.txt row i=32088 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_88_bahulaM_88"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.88", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahulaM Candasi",
    text_dev              = "बहुलं छन्दसि",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte bahulam Candasi kft hanaH karmaRi kvip",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते बहुलम् छन्दसि कृत् हनः कर्मणि क्विप्",
    padaccheda_dev        = "बहुलम् छन्दसि",
    why_dev               = "धातोः कृत्-प्रत्ययः [बहुलं छन्दसि] विहितः (३.२.88)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
