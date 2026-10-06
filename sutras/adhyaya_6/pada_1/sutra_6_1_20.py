"""
6.1.20  न वशः  —  VIDHI

Padaccheda: न वशः

न वशः (6.1.20)
Pāṭha: ashtadhyayi.com data.txt row i=61020 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_20_na_20"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.20", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.20",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na vaSaH",
    text_dev              = "न वशः",
    samagra_slp1          = "na vaSaH samprasAraRam yaNi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "न वशः सम्प्रसारणम् यङि",
    padaccheda_dev        = "न वशः",
    why_dev               = "(सूत्रम् 6.1.20) न वशः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
