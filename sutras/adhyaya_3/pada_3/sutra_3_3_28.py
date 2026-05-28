"""
3.3.28  निरभ्योः पूल्वोः  —  VIDHI

Padaccheda: निर्-अभ्योः पू-ल्वोः

krt-suffix rule: निरभ्योः पूल्वोः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_28_niraByoH_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_28_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "niraByoH pUlvoH",
    text_dev              = "निरभ्योः पूल्वोः",
    padaccheda_dev        = "निर्-अभ्योः पू-ल्वोः",
    why_dev               = "धातोः प्रत्ययः (३.3.28)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
