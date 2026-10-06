"""
8.3.115  सोढः  —  VIDHI

Padaccheda: सोढः

सोढः (8.3.115)
Pāṭha: ashtadhyayi.com data.txt row i=83115 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_115_soQaH_115"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.115", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "soQaH",
    text_dev              = "सोढः",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH soQaH saH na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः सोढः सः न",
    padaccheda_dev        = "सोढः",
    why_dev               = "(सूत्रम् 8.3.115) सोढः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
