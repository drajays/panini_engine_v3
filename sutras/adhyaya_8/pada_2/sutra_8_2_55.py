"""
8.2.55  अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः  —  VIDHI

Padaccheda: अन्-उपसर्गात् फुल्ल-क्षीब-कृश-उल्लाघाः

अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः (8.2.55)
Pāṭha: ashtadhyayi.com data.txt row i=82055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_55_anupasargA_55"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.55", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anupasargAt PullakzIbakfSollAGAH",
    text_dev              = "अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः",
    samagra_slp1          = "padasya pUrvatrAsidDam anupasargAt PullakzIbakfSollAGAH nizWAtaH naH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः निष्ठातः नः",
    padaccheda_dev        = "अन्-उपसर्गात् फुल्ल-क्षीब-कृश-उल्लाघाः",
    why_dev               = "(सूत्रम् 8.2.55) अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
