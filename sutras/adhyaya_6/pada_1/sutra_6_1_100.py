"""
6.1.100  नित्यमाम्रेडिते डाचि  —  VIDHI

Padaccheda: नित्यमाम्रेडिते डाचि

नित्यमाम्रेडिते डाचि (6.1.100)
Pāṭha: ashtadhyayi.com data.txt row i=61100 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_100_nityamAmre_100"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.100", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityamAmreqite qAci",
    text_dev              = "नित्यमाम्रेडिते डाचि",
    samagra_slp1          = "saMhitAyAm ekaH pUrvaparayoH nityam Amreqite qAci aci pararUpam avyaktAnukaraRasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् एकः पूर्वपरयोः नित्यम् आम्रेडिते डाचि अचि पररूपम् अव्यक्तानुकरणस्य",
    padaccheda_dev        = "नित्यमाम्रेडिते डाचि",
    why_dev               = "(सूत्रम् 6.1.100) नित्यमाम्रेडिते डाचि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
