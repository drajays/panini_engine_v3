"""
8.3.3  आतोऽटि नित्यम्  —  VIDHI

Padaccheda: आतः अटि नित्यम्

आतोऽटि नित्यम् (8.3.3)
Pāṭha: ashtadhyayi.com data.txt row i=83003 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_3_Atowi_3"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.3", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'Atowi nityam',
    text_dev              = 'आतोऽटि नित्यम्',
    samagra_slp1          = "atra padasya roH pUrvasya AtaH awi nityamanunAsikaH",
    samagra_dev           = "अत्र पदस्य रोः पूर्वस्य आतः अटि नित्यमनुनासिकः",
    padaccheda_dev        = "आतः अटि नित्यम्",
    why_dev               = "(सूत्रम् 8.3.3) आतोऽटि नित्यम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
