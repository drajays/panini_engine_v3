"""
8.4.10  वा भावकरणयोः  —  VIDHI

Padaccheda: वा भाव-करणयोः

वा भावकरणयोः (8.4.10)
Pāṭha: ashtadhyayi.com data.txt row i=84010 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_10_vA_10"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.10", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA BAvakaraRayoH",
    text_dev              = "वा भावकरणयोः",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm vA BAva-karaRayoH razAByAm pUrvapadAt saMjYAyAm pAnam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् वा भाव-करणयोः रषाभ्याम् पूर्वपदात् संज्ञायाम् पानम्",
    padaccheda_dev        = "वा भाव-करणयोः",
    why_dev               = "(सूत्रम् 8.4.10) वा भावकरणयोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
