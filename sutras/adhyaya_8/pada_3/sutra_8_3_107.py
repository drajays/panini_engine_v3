"""
8.3.107  सुञः  —  VIDHI

Padaccheda: सुञः

सुञः (8.3.107)
Pāṭha: ashtadhyayi.com data.txt row i=83107 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_107_suYaH_107"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.107", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suYaH",
    text_dev              = "सुञः",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH suYaH saH Candasi pUrvapadAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः सुञः सः छन्दसि पूर्वपदात्",
    padaccheda_dev        = "सुञः",
    why_dev               = "(सूत्रम् 8.3.107) सुञः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
