"""
8.2.50  निर्वाणोऽवाते  —  VIDHI

Padaccheda: निर्वाणः अवाते

निर्वाणोऽवाते (8.2.50)
Pāṭha: ashtadhyayi.com data.txt row i=82050 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_50_nirvARovA_50"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.50", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'nirvARovAte',
    text_dev              = 'निर्वाणोऽवाते',
    samagra_slp1          = "padasya pUrvatrAsidDam nirvARaH avAte nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् निर्वाणः अवाते निष्ठातः नः",
    padaccheda_dev        = "निर्वाणः अवाते",
    why_dev               = "(सूत्रम् 8.2.50) निर्वाणोऽवाते।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
