"""
3.2.184  अर्तिलूधूसूखनसहचर इत्रः  —  VIDHI

Padaccheda: अर्ति-लू-धू-सू-खन-सह-चरः इत्रः

krt-suffix rule: अर्तिलूधूसूखनसहचर इत्रः (184)
Pāṭha: ashtadhyayi.com data.txt row i=32184 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_184_artilUDUsU_184"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.184", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.184"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.184",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "artilUDUsUKanasahacara itraH",
    text_dev              = "अर्तिलूधूसूखनसहचर इत्रः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne arti-lU-DU-sU-Kana-saha-caraH itraH kft karaRe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने अर्ति-लू-धू-सू-खन-सह-चरः इत्रः कृत् करणे",
    padaccheda_dev        = "अर्ति-लू-धू-सू-खन-सह-चरः इत्रः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अर्तिलूधूसूखनसहचर इत्रः] विहितः (३.२.184)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
