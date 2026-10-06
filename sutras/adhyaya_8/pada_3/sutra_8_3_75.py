"""
8.3.75  परिस्कन्दः प्राच्यभरतेषु  —  VIDHI

Padaccheda: परिस्कन्दः प्राच्यभरतेषु

परिस्कन्दः प्राच्यभरतेषु (8.3.75)
Pāṭha: ashtadhyayi.com data.txt row i=83075 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_75_pariskanda_75"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.75", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pariskandaH prAcyaBaratezu",
    text_dev              = "परिस्कन्दः प्राच्यभरतेषु",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH pariskandaH prAcyaBaratezu saH upasargAt vA skandeH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः परिस्कन्दः प्राच्यभरतेषु सः उपसर्गात् वा स्कन्देः",
    padaccheda_dev        = "परिस्कन्दः प्राच्यभरतेषु",
    why_dev               = "(सूत्रम् 8.3.75) परिस्कन्दः प्राच्यभरतेषु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
