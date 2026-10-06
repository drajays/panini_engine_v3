"""
6.1.55  प्रजने वीयतेः  —  VIDHI

Padaccheda: प्रजने वीयतेः

प्रजने वीयतेः (6.1.55)
Pāṭha: ashtadhyayi.com data.txt row i=61055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_55_prajane_55"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.55", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prajane vIyateH",
    text_dev              = "प्रजने वीयतेः",
    samagra_slp1          = "prajane vIyateH At ecaH upadeSe viBAzA RO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रजने वीयतेः आत् एचः उपदेशे विभाषा णौ",
    padaccheda_dev        = "प्रजने वीयतेः",
    why_dev               = "(सूत्रम् 6.1.55) प्रजने वीयतेः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
