"""
3.3.128  आतो युच्  —  VIDHI

Padaccheda: आतः युच्

krt-suffix rule: आतो युच्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_128_Ato_128"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_128_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.128"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.128",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ato yuc",
    text_dev              = "आतो युच्",
    padaccheda_dev        = "आतः युच्",
    why_dev               = "धातोः प्रत्ययः (३.3.128)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
