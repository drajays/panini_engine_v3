"""
8.3.69  वेश्च स्वनो भोजने  —  VIDHI

Padaccheda: वेः च स्वनः भोजने

वेश्च स्वनो भोजने (8.3.69)
Pāṭha: ashtadhyayi.com data.txt row i=83069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_69_veSca_69"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.69", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "veSca svano Bojane",
    text_dev              = "वेश्च स्वनो भोजने",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH veH ca svanaH Bojane saH aqvyavAye api upasargAt avAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः वेः च स्वनः भोजने सः अड्व्यवाये अपि उपसर्गात् अवात्",
    padaccheda_dev        = "वेः च स्वनः भोजने",
    why_dev               = "(सूत्रम् 8.3.69) वेश्च स्वनो भोजने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
