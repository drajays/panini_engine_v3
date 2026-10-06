"""
6.3.45  उगितश्च  —  VIDHI

Padaccheda: उक्- गितः च

उगितश्च (6.3.45)
Pāṭha: ashtadhyayi.com data.txt row i=63045 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_45_ugitaSca_45"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.45", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ugitaSca",
    text_dev              = "उगितश्च",
    samagra_slp1          = "uttarapade ugitaH ca Ga-rUpa-kalpa-celaw-brUva-gotra-mata-hatezu hrasvaH nadyAH anyatarasyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे उगितः च घ-रूप-कल्प-चेलट्-ब्रूव-गोत्र-मत-हतेषु ह्रस्वः नद्याः अन्यतरस्याम्",
    padaccheda_dev        = "उक्- गितः च",
    why_dev               = "(सूत्रम् 6.3.45) उगितश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
