"""
6.1.183  दिवो झल्  —  VIDHI

Padaccheda: दिवः झल्

दिवो झल् (6.1.183)
Pāṭha: ashtadhyayi.com data.txt row i=61183 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_183_divo_183"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.183", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.183"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.183",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "divo Jal",
    text_dev              = "दिवो झल्",
    samagra_slp1          = "divaH Jal udAttaH antaH viBaktiH nAm anyatarasyAm na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "दिवः झल् उदात्तः अन्तः विभक्तिः नाम् अन्यतरस्याम् न",
    padaccheda_dev        = "दिवः झल्",
    why_dev               = "(सूत्रम् 6.1.183) दिवो झल्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
