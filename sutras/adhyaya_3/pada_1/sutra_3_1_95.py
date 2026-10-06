"""
3.1.95  कृत्याः  —  VIDHI

Padaccheda: कृत्याः प्राङ् ण्वुलः

Krt suffix rule from dhatu: कृत्याः प्राङ् ण्वुलः (95)
Pāṭha: ashtadhyayi.com data.txt row i=31095 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_95_kftyAH_95"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.95", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.95",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = 'kftyAH',
    text_dev              = 'कृत्याः',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kftyAH kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कृत्याः कृत्",
    padaccheda_dev        = "कृत्याः प्राङ् ण्वुलः",
    why_dev               = "धातोः [कृत्याः प्राङ् ण्वुलः]-प्रत्ययः विहितः (३.१.95)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
