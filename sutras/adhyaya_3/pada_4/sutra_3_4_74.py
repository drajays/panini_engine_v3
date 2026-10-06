"""
3.4.74  भीमादयोऽपादाने  —  VIDHI

Padaccheda: भीम-आदयः अपादाने

krt-suffix rule: भीमादयोऽपादाने
Pāṭha: ashtadhyayi.com data.txt row i=34074 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_74_BImAdayop_74"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.74", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'BImAdayopAdAne',
    text_dev              = 'भीमादयोऽपादाने',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BImAdayaH apAdAne kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भीमादयः अपादाने कृत्",
    padaccheda_dev        = "भीम-आदयः अपादाने",
    why_dev               = "धातोः प्रत्ययः (३.4.74)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
