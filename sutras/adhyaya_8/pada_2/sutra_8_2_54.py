"""
8.2.54  प्रस्त्योऽन्यतरस्याम्  —  VIDHI

Padaccheda: प्रस्त्यः अन्यतरस्याम्

प्रस्त्योऽन्यतरस्याम् (8.2.54)
Pāṭha: ashtadhyayi.com data.txt row i=82054 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_54_prastyony_54"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.54", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'prastyonyatarasyAm',
    text_dev              = 'प्रस्त्योऽन्यतरस्याम्',
    samagra_slp1          = "padasya pUrvatrAsidDam prastyaH anyatarasyAm nizWAtaH naH maH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् प्रस्त्यः अन्यतरस्याम् निष्ठातः नः मः",
    padaccheda_dev        = "प्रस्त्यः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.2.54) प्रस्त्योऽन्यतरस्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
