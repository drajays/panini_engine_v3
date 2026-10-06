"""
8.3.50  कःकरत्करतिकृधिकृतेष्वनदितेः  —  VIDHI

Padaccheda: कः-करत्-करति-कृधि-कृतेषु अनदितेः

कःकरत्करतिकृधिकृतेष्वनदितेः (8.3.50)
Pāṭha: ashtadhyayi.com data.txt row i=83050 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_50_kaHkaratka_50"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.50", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaHkaratkaratikfDikftezvanaditeH",
    text_dev              = "कःकरत्करतिकृधिकृतेष्वनदितेः",
    samagra_slp1          = "padasya pUrvatrAsidDam saMhitAyAm kaH-karat-karati-kfDi-kftezu anaditeH visarjanIyasya kupvoH saH samAse Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् संहितायाम् कः-करत्-करति-कृधि-कृतेषु अनदितेः विसर्जनीयस्य कुप्वोः सः समासे छन्दसि",
    padaccheda_dev        = "कः-करत्-करति-कृधि-कृतेषु अनदितेः",
    why_dev               = "(सूत्रम् 8.3.50) कःकरत्करतिकृधिकृतेष्वनदितेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
