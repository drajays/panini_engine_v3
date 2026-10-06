"""
8.4.28  उपसर्गाद् बहुलम्  —  VIDHI

Padaccheda: उपसर्गात् अन्-ओत्-परः

उपसर्गाद् बहुलम् (8.4.28)
Pāṭha: ashtadhyayi.com data.txt row i=84028 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_28_upasargAd_28"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.28", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargAd bahulam",
    text_dev              = "उपसर्गाद् बहुलम्",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm upasargAt anotparaH razAByAm naH ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् उपसर्गात् अनोत्परः रषाभ्याम् नः च",
    padaccheda_dev        = "उपसर्गात् अन्-ओत्-परः",
    why_dev               = "(सूत्रम् 8.4.28) उपसर्गाद् बहुलम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
