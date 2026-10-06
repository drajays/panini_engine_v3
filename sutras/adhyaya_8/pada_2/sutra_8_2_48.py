"""
8.2.48  अञ्चोऽनपादाने  —  VIDHI

Padaccheda: अञ्चः अन्-अपादाने

अञ्चोऽनपादाने (8.2.48)
Pāṭha: ashtadhyayi.com data.txt row i=82048 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_48_aYconapAd_48"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.48", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'aYconapAdAne',
    text_dev              = 'अञ्चोऽनपादाने',
    samagra_slp1          = "padasya pUrvatrAsidDam aYcaH anapAdAne nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् अञ्चः अनपादाने निष्ठातः नः",
    padaccheda_dev        = "अञ्चः अन्-अपादाने",
    why_dev               = "(सूत्रम् 8.2.48) अञ्चोऽनपादाने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
