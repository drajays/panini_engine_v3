"""
6.4.42  जनसनखनां सञ्झलोः  —  VIDHI

Padaccheda: जन-सन-खनाम् सन्-झलोः

जनसनखनां सञ्झलोः (6.4.42)
Pāṭha: ashtadhyayi.com data.txt row i=64042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_42_janasanaKa_42"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.42", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "janasanaKanAM saYJaloH",
    text_dev              = "जनसनखनां सञ्झलोः",
    samagra_slp1          = "aNgasya asidDavadatrABAt jana-sana-KanAm san-JaloH nalopaH At",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् जन-सन-खनाम् सन्-झलोः नलोपः आत्",
    padaccheda_dev        = "जन-सन-खनाम् सन्-झलोः",
    why_dev               = "(सूत्रम् 6.4.42) जनसनखनां सञ्झलोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
