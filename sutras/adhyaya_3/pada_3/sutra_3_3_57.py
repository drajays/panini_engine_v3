"""
3.3.57  ऋदोरप्  —  VIDHI

Padaccheda: ॠत्-ओः अप्

krt-suffix rule: ऋदोरप्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_57_fdorap_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_57_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fdorap",
    text_dev              = "ऋदोरप्",
    padaccheda_dev        = "ॠत्-ओः अप्",
    why_dev               = "धातोः प्रत्ययः (३.3.57)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
