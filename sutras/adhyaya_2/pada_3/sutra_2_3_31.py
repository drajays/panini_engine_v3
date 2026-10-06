"""
2.3.31  एनपा द्वितीया  —  VIDHI

Padaccheda: एनपा द्वितीया

ena-type pronoun takes dvitiya.
Pāṭha: ashtadhyayi.com data.txt row i=23031 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_31_enapa_dvitiya"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "enapA dvitIyA",
    text_dev              = "एनपा द्वितीया",
    samagra_slp1          = "anaBihite enapA dvitIyA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनभिहिते एनपा द्वितीया",
    padaccheda_dev        = "एनपा द्वितीया",
    why_dev               = "एनपा द्वितीया (२.३.३१)।",
    anuvritti_from        = ('2.3.2',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
