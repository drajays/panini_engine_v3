"""
8.2.59  भित्तं शकलम्  —  VIDHI

Padaccheda: भित्तम् शकलम्

भित्तं शकलम् (8.2.59)
Pāṭha: ashtadhyayi.com data.txt row i=82059 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_59_BittaM_59"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.59", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BittaM Sakalam",
    text_dev              = "भित्तं शकलम्",
    samagra_slp1          = "padasya pUrvatrAsidDam Bittam Sakalam nizWAtaH naH na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् भित्तम् शकलम् निष्ठातः नः न",
    padaccheda_dev        = "भित्तम् शकलम्",
    why_dev               = "(सूत्रम् 8.2.59) भित्तं शकलम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
