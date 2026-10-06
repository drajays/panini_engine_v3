"""
3.2.99  उपसर्गे च संज्ञायाम्  —  VIDHI

Padaccheda: उपसर्गे च संज्ञायाम्

krt-suffix rule: उपसर्गे च संज्ञायाम् (99)
Pāṭha: ashtadhyayi.com data.txt row i=32099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_99_upasarge_99"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.99", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasarge ca saMjYAyAm",
    text_dev              = "उपसर्गे च संज्ञायाम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte upasarge ca saMjYAyAm kft janeH qaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते उपसर्गे च संज्ञायाम् कृत् जनेः डः",
    padaccheda_dev        = "उपसर्गे च संज्ञायाम्",
    why_dev               = "धातोः कृत्-प्रत्ययः [उपसर्गे च संज्ञायाम्] विहितः (३.२.99)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
