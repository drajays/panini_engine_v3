"""
3.4.44  ऊर्ध्वे शुषिपूरोः  —  VIDHI

Padaccheda: ऊर्ध्वे शुषि-पूरोः

krt-suffix rule: ऊर्ध्वे शुषिपूरोः
Pāṭha: ashtadhyayi.com data.txt row i=34044 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_44_UrDve_44"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.44", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UrDve SuzipUroH",
    text_dev              = "ऊर्ध्वे शुषिपूरोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH UrDve Suzi-pUroH kft Ramul kartroH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः ऊर्ध्वे शुषि-पूरोः कृत् णमुल् कर्त्रोः",
    padaccheda_dev        = "ऊर्ध्वे शुषि-पूरोः",
    why_dev               = "धातोः प्रत्ययः (३.4.44)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
