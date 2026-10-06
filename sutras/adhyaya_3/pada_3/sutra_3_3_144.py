"""
3.3.144  किंवृत्ते लिङ्लृटौ  —  VIDHI

Padaccheda: किंवृत्ते लिङ्-लृटौ

krt-suffix rule: किंवृत्ते लिङ्लृटौ
Pāṭha: ashtadhyayi.com data.txt row i=33144 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_144_kiMvftte_144"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.144", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.144"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.144",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kiMvftte liNlfwO",
    text_dev              = "किंवृत्ते लिङ्लृटौ",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kiMvftte liNlfwO kft utApyoH garhAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः किंवृत्ते लिङ्लृटौ कृत् उताप्योः गर्हायाम्",
    padaccheda_dev        = "किंवृत्ते लिङ्-लृटौ",
    why_dev               = "धातोः प्रत्ययः (३.3.144)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
