"""
8.2.52  पचो वः  —  VIDHI

Padaccheda: पचः वः

पचो वः (8.2.52)
Pāṭha: ashtadhyayi.com data.txt row i=82052 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_52_paco_52"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.52", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paco vaH",
    text_dev              = "पचो वः",
    samagra_slp1          = "padasya pUrvatrAsidDam pacaH vaH nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् पचः वः निष्ठातः नः",
    padaccheda_dev        = "पचः वः",
    why_dev               = "(सूत्रम् 8.2.52) पचो वः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
