"""
6.2.88  मालादीनां च  —  VIDHI

Padaccheda: माला-आदीनाम् च

मालाऽऽदीनां च (6.2.88)
Pāṭha: ashtadhyayi.com data.txt row i=62088 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_88_mAlAdInA_88"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.88", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'mAlAdInAM ca',
    text_dev              = 'मालादीनां च',
    samagra_slp1          = "AdiH udAttaH mAlA-AdInAm ca pUrvapadam prasTe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आदिः उदात्तः माला-आदीनाम् च पूर्वपदम् प्रस्थे",
    padaccheda_dev        = "माला-आदीनाम् च",
    why_dev               = "(सूत्रम् 6.2.88) मालाऽऽदीनां च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
