"""
3.4.51  प्रमाणे च  —  VIDHI

Padaccheda: प्रमाणे च

krt-suffix rule: प्रमाणे च
Pāṭha: ashtadhyayi.com data.txt row i=34051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_51_pramARe_51"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.51", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pramARe ca",
    text_dev              = "प्रमाणे च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH pramARe ca kft Ramul tftIyAyAm saptamyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः प्रमाणे च कृत् णमुल् तृतीयायाम् सप्तम्याम्",
    padaccheda_dev        = "प्रमाणे च",
    why_dev               = "धातोः प्रत्ययः (३.4.51)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
