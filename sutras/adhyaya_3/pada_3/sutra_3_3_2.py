"""
3.3.2  भूतेऽपि दृश्यन्ते  —  VIDHI

Padaccheda: भूते अपि दृश्यन्ते (क्रियापदम्)

krt-suffix rule: भूतेऽपि दृश्यन्ते
Pāṭha: ashtadhyayi.com data.txt row i=33002 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_2_BUtepi_2"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.2", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'BUtepi dfSyante',
    text_dev              = 'भूतेऽपि दृश्यन्ते',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte api dfSyante kft uRAdayaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते अपि दृश्यन्ते कृत् उणादयः",
    padaccheda_dev        = "भूते अपि दृश्यन्ते (क्रियापदम्)",
    why_dev               = "धातोः प्रत्ययः (३.3.2)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
