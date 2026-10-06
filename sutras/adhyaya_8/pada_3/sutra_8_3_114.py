"""
8.3.114  प्रतिस्तब्धनिस्तब्धौ च  —  VIDHI

Padaccheda: प्रतिस्तब्ध-निस्तब्धौ च

प्रतिस्तब्धनिस्तब्धौ च (8.3.114)
Pāṭha: ashtadhyayi.com data.txt row i=83114 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_114_pratistabD_114"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.114", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.114"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratistabDanistabDO ca",
    text_dev              = "प्रतिस्तब्धनिस्तब्धौ च",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH pratistabDa-nistabDO ca saH na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः प्रतिस्तब्ध-निस्तब्धौ च सः न",
    padaccheda_dev        = "प्रतिस्तब्ध-निस्तब्धौ च",
    why_dev               = "(सूत्रम् 8.3.114) प्रतिस्तब्धनिस्तब्धौ च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
