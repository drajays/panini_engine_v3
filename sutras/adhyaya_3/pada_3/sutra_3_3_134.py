"""
3.3.134  आशंसावचने लिङ्  —  VIDHI

Padaccheda: आशंसावचने लिङ्

krt-suffix rule: आशंसावचने लिङ्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_134_ASaMsAvaca_134"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_134_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.134"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.134",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASaMsAvacane liN",
    text_dev              = "आशंसावचने लिङ्",
    padaccheda_dev        = "आशंसावचने लिङ्",
    why_dev               = "धातोः प्रत्ययः (३.3.134)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
