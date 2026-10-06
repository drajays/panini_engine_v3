"""
8.3.67  स्तम्भेः  —  VIDHI

Padaccheda: स्तन्भेः

स्तम्भेः (8.3.67)
Pāṭha: ashtadhyayi.com data.txt row i=83067 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_67_stamBeH_67"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.67", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stamBeH",
    text_dev              = "स्तम्भेः",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH stamBeH saH aqvyavAye api upasargAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः स्तम्भेः सः अड्व्यवाये अपि उपसर्गात्",
    padaccheda_dev        = "स्तन्भेः",
    why_dev               = "(सूत्रम् 8.3.67) स्तम्भेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
