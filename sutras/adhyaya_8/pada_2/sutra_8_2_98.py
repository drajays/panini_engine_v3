"""
8.2.98  पूर्वं तु भाषायाम्  —  VIDHI

Padaccheda: पूर्वम् तु भाषायाम्

पूर्वं तु भाषायाम् (8.2.98)
Pāṭha: ashtadhyayi.com data.txt row i=82098 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_98_pUrvaM_98"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.98", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvaM tu BAzAyAm",
    text_dev              = "पूर्वं तु भाषायाम्",
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH pUrvam tu BAzAyAm vicAryamARAnAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः पूर्वम् तु भाषायाम् विचार्यमाणानाम्",
    padaccheda_dev        = "पूर्वम् तु भाषायाम्",
    why_dev               = "(सूत्रम् 8.2.98) पूर्वं तु भाषायाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
