"""
8.2.96  अङ्गयुक्तं तिङ् आकाङ्क्षम्  —  VIDHI

Padaccheda: अङ्गयुक्तम् तिङ् आकाङ्क्षम्

अङ्गयुक्तं तिङ् आकाङ्क्षम् (8.2.96)
Pāṭha: ashtadhyayi.com data.txt row i=82096 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_96_aNgayuktaM_96"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.96", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aNgayuktaM tiN AkANkzam",
    text_dev              = "अङ्गयुक्तं तिङ् आकाङ्क्षम्",
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH aNgayuktam tiN AkANkzam Bartsane",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः अङ्गयुक्तम् तिङ् आकाङ्क्षम् भर्त्सने",
    padaccheda_dev        = "अङ्गयुक्तम् तिङ् आकाङ्क्षम्",
    why_dev               = "(सूत्रम् 8.2.96) अङ्गयुक्तं तिङ् आकाङ्क्षम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
