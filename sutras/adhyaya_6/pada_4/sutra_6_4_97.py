"""
6.4.97  इस्मन्त्रन्क्विषु च  —  VIDHI

Padaccheda: इस्-मन्-त्रन्-क्विषु च

इस्मन्त्रन्क्विषु च (6.4.97)
Pāṭha: ashtadhyayi.com data.txt row i=64097 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_97_ismantrank_97"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.97", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ismantrankvizu ca",
    text_dev              = "इस्मन्त्रन्क्विषु च",
    samagra_slp1          = "aNgasya asidDavadatrABAt is-man-tran-kvizu ca aci upaDAyAH hrasvaH CAdeH Ge",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् इस्-मन्-त्रन्-क्विषु च अचि उपधायाः ह्रस्वः छादेः घे",
    padaccheda_dev        = "इस्-मन्-त्रन्-क्विषु च",
    why_dev               = "(सूत्रम् 6.4.97) इस्मन्त्रन्क्विषु च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
