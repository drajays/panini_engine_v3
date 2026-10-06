"""
8.3.54  इडाया वा  —  VIDHI

Padaccheda: इडायाः वा

इडाया वा (8.3.54)
Pāṭha: ashtadhyayi.com data.txt row i=83054 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_54_iqAyA_54"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.54", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iqAyA vA",
    text_dev              = "इडाया वा",
    samagra_slp1          = "padasya pUrvatrAsidDam saMhitAyAm iqAyAH vA visarjanIyasya kupvoH saH samAse Candasi zazWyAH patiputrapfzWapArapadapayaspozezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् संहितायाम् इडायाः वा विसर्जनीयस्य कुप्वोः सः समासे छन्दसि षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु",
    padaccheda_dev        = "इडायाः वा",
    why_dev               = "(सूत्रम् 8.3.54) इडाया वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
