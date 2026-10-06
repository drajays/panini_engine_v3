"""
6.4.50  क्यस्य विभाषा  —  VIDHI

Padaccheda: क्यस्य विभाषा

क्यस्य विभाषा (6.4.50)
Pāṭha: ashtadhyayi.com data.txt row i=64050 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_50_kyasya_50"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.50", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kyasya viBAzA",
    text_dev              = "क्यस्य विभाषा",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke kyasya viBAzA nalopaH lopaH halaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके क्यस्य विभाषा नलोपः लोपः हलः",
    padaccheda_dev        = "क्यस्य विभाषा",
    why_dev               = "(सूत्रम् 6.4.50) क्यस्य विभाषा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
