"""
8.2.58  वित्तो भोगप्रत्यययोः  —  VIDHI

Padaccheda: वित्तः भोगप्रत्यययोः

वित्तो भोगप्रत्यययोः (8.2.58)
Pāṭha: ashtadhyayi.com data.txt row i=82058 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_58_vitto_58"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.58", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vitto BogapratyayayoH",
    text_dev              = "वित्तो भोगप्रत्यययोः",
    samagra_slp1          = "padasya pUrvatrAsidDam vittaH BogapratyayayoH nizWAtaH naH na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वित्तः भोगप्रत्यययोः निष्ठातः नः न",
    padaccheda_dev        = "वित्तः भोगप्रत्यययोः",
    why_dev               = "(सूत्रम् 8.2.58) वित्तो भोगप्रत्यययोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
