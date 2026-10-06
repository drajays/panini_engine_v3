"""
8.3.70  परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम्  —  VIDHI

Padaccheda: परि-नि-विभ्यः सेव-सित-सय-सिवु-सह-सुट्‍-स्तु-स्वञ्जाम्

परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम् (8.3.70)
Pāṭha: ashtadhyayi.com data.txt row i=83070 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_70_pariniviBy_70"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.70", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pariniviByaH sevasitasayasivusahasuwstusvaYjAm",
    text_dev              = "परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम्",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH pari-ni-viByaH seva-sita-saya-sivu-saha-suw-stu-svaYjAm saH aqvyavAye api upasargAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः परि-नि-विभ्यः सेव-सित-सय-सिवु-सह-सुट्-स्तु-स्वञ्जाम् सः अड्व्यवाये अपि उपसर्गात्",
    padaccheda_dev        = "परि-नि-विभ्यः सेव-सित-सय-सिवु-सह-सुट्‍-स्तु-स्वञ्जाम्",
    why_dev               = "(सूत्रम् 8.3.70) परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
