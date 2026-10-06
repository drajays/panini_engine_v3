"""
3.3.160  इच्छार्थेभ्यो विभाषा वर्तमाने  —  VIDHI

Padaccheda: इच्छार्थेभ्यः विभाषा वर्त्तमाने

krt-suffix rule: इच्छार्थेभ्यो विभाषा वर्तमाने
Pāṭha: ashtadhyayi.com data.txt row i=33160 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_160_icCArTeByo_160"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.160", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.160"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.160",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "icCArTeByo viBAzA vartamAne",
    text_dev              = "इच्छार्थेभ्यो विभाषा वर्तमाने",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH icCArTeByo viBAzA varttamAne kft liN",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः इच्छार्थेभ्यो विभाषा वर्त्तमाने कृत् लिङ्",
    padaccheda_dev        = "इच्छार्थेभ्यः विभाषा वर्त्तमाने",
    why_dev               = "धातोः प्रत्ययः (३.3.160)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
