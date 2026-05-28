"""
3.3.46  प्रे लिप्सायाम्  —  VIDHI

Padaccheda: प्रे लिप्सायाम्

krt-suffix rule: प्रे लिप्सायाम्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_46_pre_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_46_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pre lipsAyAm",
    text_dev              = "प्रे लिप्सायाम्",
    padaccheda_dev        = "प्रे लिप्सायाम्",
    why_dev               = "धातोः प्रत्ययः (३.3.46)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
