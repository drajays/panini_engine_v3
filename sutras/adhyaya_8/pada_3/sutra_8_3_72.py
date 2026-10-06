"""
8.3.72  अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु  —  VIDHI

Padaccheda: अनु-वि-परि-अभि-निभ्यः स्यन्दतेः अप्राणिषु

अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु (8.3.72)
Pāṭha: ashtadhyayi.com data.txt row i=83072 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_72_anuviparya_72"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.72", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anuviparyaBiniByaH syandateraprARizu",
    text_dev              = "अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH anu-vi-pari-aBi-niByaH syandateH aprARizu saH upasargAt vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः अनु-वि-परि-अभि-निभ्यः स्यन्दतेः अप्राणिषु सः उपसर्गात् वा",
    padaccheda_dev        = "अनु-वि-परि-अभि-निभ्यः स्यन्दतेः अप्राणिषु",
    why_dev               = "(सूत्रम् 8.3.72) अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
