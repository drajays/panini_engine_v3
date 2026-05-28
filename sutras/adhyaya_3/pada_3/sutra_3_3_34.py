"""
3.3.34  छन्दोनाम्नि च  —  VIDHI

Padaccheda: छन्दोनाम्नि च

krt-suffix rule: छन्दोनाम्नि च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_34_CandonAmni_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandonAmni ca",
    text_dev              = "छन्दोनाम्नि च",
    padaccheda_dev        = "छन्दोनाम्नि च",
    why_dev               = "धातोः प्रत्ययः (३.3.34)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
