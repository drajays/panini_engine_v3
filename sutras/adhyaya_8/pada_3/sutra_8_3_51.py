"""
8.3.51  पञ्चम्याः परावध्यर्थे  —  VIDHI

Padaccheda: पञ्चम्याः परौ अधि-अर्थे

पञ्चम्याः परावध्यर्थे (8.3.51)
Pāṭha: ashtadhyayi.com data.txt row i=83051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_51_paYcamyAH_51"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.51", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paYcamyAH parAvaDyarTe",
    text_dev              = "पञ्चम्याः परावध्यर्थे",
    samagra_slp1          = "padasya pUrvatrAsidDam saMhitAyAm paYcamyAH parO aDyarTe visarjanIyasya kupvoH saH samAse Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् संहितायाम् पञ्चम्याः परौ अध्यर्थे विसर्जनीयस्य कुप्वोः सः समासे छन्दसि",
    padaccheda_dev        = "पञ्चम्याः परौ अधि-अर्थे",
    why_dev               = "(सूत्रम् 8.3.51) पञ्चम्याः परावध्यर्थे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
