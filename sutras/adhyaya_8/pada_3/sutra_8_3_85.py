"""
8.3.85  मातुःपितुर्भ्यामन्यतरस्याम्  —  VIDHI

Padaccheda: मातुः-पितुर्भ्याम् अन्यतरस्याम्

मातुःपितुर्भ्यामन्यतरस्याम् (8.3.85)
Pāṭha: ashtadhyayi.com data.txt row i=83085 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_85_mAtuHpitur_85"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.85", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mAtuHpiturByAmanyatarasyAm",
    text_dev              = "मातुःपितुर्भ्यामन्यतरस्याम्",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH mAtuH-piturByAm anyatarasyAm saH samAse svasA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः मातुः-पितुर्भ्याम् अन्यतरस्याम् सः समासे स्वसा",
    padaccheda_dev        = "मातुः-पितुर्भ्याम् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.3.85) मातुःपितुर्भ्यामन्यतरस्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
