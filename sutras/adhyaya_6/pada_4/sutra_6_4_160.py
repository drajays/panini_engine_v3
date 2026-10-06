"""
6.4.160  ज्यादादीयसः  —  VIDHI

Padaccheda: ज्यात् आत् ईयसः

ज्यादादीयसः (6.4.160)
Pāṭha: ashtadhyayi.com data.txt row i=64160 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_160_jyAdAdIyas_160"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.160", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.160"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.160",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jyAdAdIyasaH",
    text_dev              = "ज्यादादीयसः",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya jyAt At IyasaH izWa-iman-Iyassu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य ज्यात् आत् ईयसः इष्ठ-इमन्-ईयस्सु",
    padaccheda_dev        = "ज्यात् आत् ईयसः",
    why_dev               = "(सूत्रम् 6.4.160) ज्यादादीयसः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
