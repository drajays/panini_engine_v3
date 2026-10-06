"""
3.4.53  द्वितीयायां च  —  VIDHI

Padaccheda: द्वितीयायाम् च

krt-suffix rule: द्वितीयायां च
Pāṭha: ashtadhyayi.com data.txt row i=34053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_53_dvitIyAyAM_53"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.53", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvitIyAyAM ca",
    text_dev              = "द्वितीयायां च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH dvitIyAyAm ca kft Ramul parIpsAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः द्वितीयायाम् च कृत् णमुल् परीप्सायाम्",
    padaccheda_dev        = "द्वितीयायाम् च",
    why_dev               = "धातोः प्रत्ययः (३.4.53)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
