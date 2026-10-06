"""
8.2.56  नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्  —  VIDHI

Padaccheda: नुद-विद-उन्द-त्रा-घ्रा-ह्रीभ्यः अन्यतरस्याम्

नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम् (8.2.56)
Pāṭha: ashtadhyayi.com data.txt row i=82056 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_56_nudavidond_56"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.56", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'nudavidondatrAGrAhrIByonyatarasyAm',
    text_dev              = 'नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्',
    samagra_slp1          = "padasya pUrvatrAsidDam nudavidondatrAGrAhrIByaH anyatarasyAm nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् नुदविदोन्दत्राघ्राह्रीभ्यः अन्यतरस्याम् निष्ठातः नः",
    padaccheda_dev        = "नुद-विद-उन्द-त्रा-घ्रा-ह्रीभ्यः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.2.56) नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
