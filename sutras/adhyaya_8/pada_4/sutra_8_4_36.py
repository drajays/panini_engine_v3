"""
8.4.36  नशेः षान्तस्य  —  VIDHI

Padaccheda: नशेः ष-अन्तस्य

नशेः षान्तस्य (8.4.36)
Pāṭha: ashtadhyayi.com data.txt row i=84036 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_36_naSeH_36"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.36", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naSeH zAntasya",
    text_dev              = "नशेः षान्तस्य",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm naSeH zAntasya razAByAm na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् नशेः षान्तस्य रषाभ्याम् न",
    padaccheda_dev        = "नशेः ष-अन्तस्य",
    why_dev               = "(सूत्रम् 8.4.36) नशेः षान्तस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
