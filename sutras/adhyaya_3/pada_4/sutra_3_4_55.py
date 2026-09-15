"""
3.4.55  परिक्लिश्यमाने च  —  VIDHI

Padaccheda: परिक्लिश्यमाने च

krt-suffix rule: परिक्लिश्यमाने च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_55_parikliSya_55"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.55", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parikliSyamAne ca",
    text_dev              = "परिक्लिश्यमाने च",
    padaccheda_dev        = "परिक्लिश्यमाने च",
    why_dev               = "धातोः प्रत्ययः (३.4.55)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
