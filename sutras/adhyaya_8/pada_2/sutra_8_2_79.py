"""
8.2.79  न भकुर्छुराम्  —  VIDHI

Padaccheda: न भ-कुर्-छुराम्

न भकुर्छुराम् (8.2.79)
Pāṭha: ashtadhyayi.com data.txt row i=82079 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_79_na_79"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.79", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.79"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.79",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na BakurCurAm",
    text_dev              = "न भकुर्छुराम्",
    samagra_slp1          = "padasya pUrvatrAsidDam na BakurCurAm DAtoH rvoH dIrGa",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् न भकुर्छुराम् धातोः र्वोः दीर्घ",
    padaccheda_dev        = "न भ-कुर्-छुराम्",
    why_dev               = "(सूत्रम् 8.2.79) न भकुर्छुराम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
