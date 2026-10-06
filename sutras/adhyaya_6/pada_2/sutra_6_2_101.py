"""
6.2.101  न हास्तिनफलकमार्देयाः  —  VIDHI

Padaccheda: न हास्तिन-फलक-मार्देयाः

न हास्तिनफलकमार्देयाः (6.2.101)
Pāṭha: ashtadhyayi.com data.txt row i=62101 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_101_na_101"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.101", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.101"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.101",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na hAstinaPalakamArdeyAH",
    text_dev              = "न हास्तिनफलकमार्देयाः",
    samagra_slp1          = "udAttaH antaH na hAstina-Palaka-mArdeyAH pUrvapadam pure",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः अन्तः न हास्तिन-फलक-मार्देयाः पूर्वपदम् पुरे",
    padaccheda_dev        = "न हास्तिन-फलक-मार्देयाः",
    why_dev               = "(सूत्रम् 6.2.101) न हास्तिनफलकमार्देयाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
