"""
8.2.101  चिदिति चोपमाऽर्थे प्रयुज्यमाने  —  VIDHI

Padaccheda: चित् ति च उपमा-अर्थे प्रयुज्यमाने

चिदिति चोपमाऽर्थे प्रयुज्यमाने (8.2.101)
Pāṭha: ashtadhyayi.com data.txt row i=82101 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_101_ciditi_101"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.101", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.101"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.101",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'ciditi copamArTe prayujyamAne',
    text_dev              = 'चिदिति चोपमाऽर्थे प्रयुज्यमाने',
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH cit iti ca upamArTe prayujyamAne anudAttam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः चित् इति च उपमाऽर्थे प्रयुज्यमाने अनुदात्तम्",
    padaccheda_dev        = "चित् ति च उपमा-अर्थे प्रयुज्यमाने",
    why_dev               = "(सूत्रम् 8.2.101) चिदिति चोपमाऽर्थे प्रयुज्यमाने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
