"""
3.4.58  नाम्न्यादिशिग्रहोः  —  VIDHI

Padaccheda: नाम्नि आदिशि-ग्रहोः

krt-suffix rule: नाम्न्यादिशिग्रहोः
Pāṭha: ashtadhyayi.com data.txt row i=34058 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_58_nAmnyAdiSi_58"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.58", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAmnyAdiSigrahoH",
    text_dev              = "नाम्न्यादिशिग्रहोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH nAmni AdiSi-grahoH kft Ramul dvitIyAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः नाम्नि आदिशि-ग्रहोः कृत् णमुल् द्वितीयायाम्",
    padaccheda_dev        = "नाम्नि आदिशि-ग्रहोः",
    why_dev               = "धातोः प्रत्ययः (३.4.58)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
