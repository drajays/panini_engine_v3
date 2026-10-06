"""
8.3.87  उपसर्गप्रादुर्भ्यामस्तिर्यच्परः  —  VIDHI

Padaccheda: उपसर्ग-प्रादुर्भ्याम् अस्तिः य्-अच्-परः

उपसर्गप्रादुर्भ्यामस्तिर्यच्परः (8.3.87)
Pāṭha: ashtadhyayi.com data.txt row i=83087 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_87_upasargapr_87"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.87", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargaprAdurByAmastiryacparaH",
    text_dev              = "उपसर्गप्रादुर्भ्यामस्तिर्यच्परः",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH upasarga-prAdurByAm astiH yacparaH saH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः उपसर्ग-प्रादुर्भ्याम् अस्तिः यच्परः सः",
    padaccheda_dev        = "उपसर्ग-प्रादुर्भ्याम् अस्तिः य्-अच्-परः",
    why_dev               = "(सूत्रम् 8.3.87) उपसर्गप्रादुर्भ्यामस्तिर्यच्परः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
