"""
8.3.94  छन्दोनाम्नि च  —  VIDHI

Padaccheda: छन्दोनाम्नि च

छन्दोनाम्नि च (8.3.94)
Pāṭha: ashtadhyayi.com data.txt row i=83094 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_94_CandonAmni_94"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.94", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandonAmni ca",
    text_dev              = "छन्दोनाम्नि च",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH CandonAmni ca saH vizwaraH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः छन्दोनाम्नि च सः विष्टरः",
    padaccheda_dev        = "छन्दोनाम्नि च",
    why_dev               = "(सूत्रम् 8.3.94) छन्दोनाम्नि च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
