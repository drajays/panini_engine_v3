"""
3.1.131  अग्नौ परिचाय्योपचाय्यसमूह्याः  —  VIDHI

Padaccheda: अग्नौ परिचाय्य-उपचाय्य-समूह्याः

Krt suffix rule from dhatu: अग्नौ परिचाय्योपचाय्यसमूह्याः (131)
Pāṭha: ashtadhyayi.com data.txt row i=31131 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_131_agnO_131"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.131", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "agnO paricAyyopacAyyasamUhyAH",
    text_dev              = "अग्नौ परिचाय्योपचाय्यसमूह्याः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH agnO paricAyya-upacAyya-samUhyAH kft Ryat",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः अग्नौ परिचाय्य-उपचाय्य-समूह्याः कृत् ण्यत्",
    padaccheda_dev        = "अग्नौ परिचाय्य-उपचाय्य-समूह्याः",
    why_dev               = "धातोः [अग्नौ परिचाय्योपचाय्यसमूह्याः]-प्रत्ययः विहितः (३.१.131)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
