"""
3.4.7  लिङर्थे लेट्  —  VIDHI

Padaccheda: लिङ्-अर्थे लेट्

krt-suffix rule: लिङर्थे लेट्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_7_liNarTe_7"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.7", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "liNarTe lew",
    text_dev              = "लिङर्थे लेट्",
    padaccheda_dev        = "लिङ्-अर्थे लेट्",
    why_dev               = "धातोः प्रत्ययः (३.4.7)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
