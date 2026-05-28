"""
3.3.76  हनश्च वधः  —  VIDHI

Padaccheda: हनः च वधः

krt-suffix rule: हनश्च वधः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_76_hanaSca_76"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hanaSca vaDaH",
    text_dev              = "हनश्च वधः",
    padaccheda_dev        = "हनः च वधः",
    why_dev               = "धातोः प्रत्ययः (३.3.76)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
