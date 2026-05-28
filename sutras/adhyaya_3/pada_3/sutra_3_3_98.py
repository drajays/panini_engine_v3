"""
3.3.98  व्रजयजोर्भावे क्यप्  —  VIDHI

Padaccheda: व्रज-यजोः भावे क्यप्

krt-suffix rule: व्रजयजोर्भावे क्यप्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_98_vrajayajor_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_98_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vrajayajorBAve kyap",
    text_dev              = "व्रजयजोर्भावे क्यप्",
    padaccheda_dev        = "व्रज-यजोः भावे क्यप्",
    why_dev               = "धातोः प्रत्ययः (३.3.98)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
