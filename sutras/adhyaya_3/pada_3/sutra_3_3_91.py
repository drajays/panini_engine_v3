"""
3.3.91  स्वपो नन्  —  VIDHI

Padaccheda: स्वपः नन्

krt-suffix rule: स्वपो नन्
Pāṭha: ashtadhyayi.com data.txt row i=33091 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_91_svapo_91"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.91", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svapo nan",
    text_dev              = "स्वपो नन्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm svapaH nan kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्वपः नन् कृत्",
    padaccheda_dev        = "स्वपः नन्",
    why_dev               = "धातोः प्रत्ययः (३.3.91)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
