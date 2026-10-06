"""
6.1.161  अनुदात्तस्य च यत्रोदात्तलोपः  —  VIDHI

Padaccheda: अनुदात्तस्य च यत्र उदात्त-लोपः

अनुदात्तस्य च यत्रोदात्तलोपः (6.1.161)
Pāṭha: ashtadhyayi.com data.txt row i=61161 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_161_anudAttasy_161"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.161", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.161"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.161",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anudAttasya ca yatrodAttalopaH",
    text_dev              = "अनुदात्तस्य च यत्रोदात्तलोपः",
    samagra_slp1          = "anudAttasya ca yatra udAttalopaH antaH udAttaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनुदात्तस्य च यत्र उदात्तलोपः अन्तः उदात्तः",
    padaccheda_dev        = "अनुदात्तस्य च यत्र उदात्त-लोपः",
    why_dev               = "(सूत्रम् 6.1.161) अनुदात्तस्य च यत्रोदात्तलोपः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
