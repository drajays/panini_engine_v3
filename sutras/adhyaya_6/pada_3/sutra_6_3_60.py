"""
6.3.60  मन्थौदनसक्तुबिन्दुवज्रभारहारवीवधगाहेषु च  —  VIDHI

Padaccheda: मन्थ-ओदन-सक्तु-बिन्दु-वज्र-भार-हार-वीवध-गाहेषु च

मन्थौदनसक्तुबिन्दुवज्रभारहारवीवधगाहेषु च (6.3.60)
Pāṭha: ashtadhyayi.com data.txt row i=63060 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_60_manTOdanas_60"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.60", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "manTOdanasaktubinduvajraBArahAravIvaDagAhezu ca",
    text_dev              = "मन्थौदनसक्तुबिन्दुवज्रभारहारवीवधगाहेषु च",
    samagra_slp1          = "uttarapade manTa-odana-saktu-bindu-vajra-BAra-hAra-vIvaDa-gAhezu ca treH udakasya udaH anyatarasyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे मन्थ-ओदन-सक्तु-बिन्दु-वज्र-भार-हार-वीवध-गाहेषु च त्रेः उदकस्य उदः अन्यतरस्याम्",
    padaccheda_dev        = "मन्थ-ओदन-सक्तु-बिन्दु-वज्र-भार-हार-वीवध-गाहेषु च",
    why_dev               = "(सूत्रम् 6.3.60) मन्थौदनसक्तुबिन्दुवज्रभारहारवीवधगाहेषु च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
