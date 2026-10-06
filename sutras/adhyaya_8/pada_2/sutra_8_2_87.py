"""
8.2.87  ओमभ्यादाने  —  VIDHI

Padaccheda: ओम् अभ्यादाने

ओमभ्यादाने (8.2.87)
Pāṭha: ashtadhyayi.com data.txt row i=82087 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_87_omaByAdAne_87"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.87", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "omaByAdAne",
    text_dev              = "ओमभ्यादाने",
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH om aByAdAne",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः ओम् अभ्यादाने",
    padaccheda_dev        = "ओम् अभ्यादाने",
    why_dev               = "(सूत्रम् 8.2.87) ओमभ्यादाने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
