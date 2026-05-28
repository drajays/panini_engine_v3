"""
3.3.16  पदरुजविशस्पृशो घञ्  —  VIDHI

Padaccheda: पदरुज-विश-स्पृशः घञ्

krt-suffix rule: पदरुजविशस्पृशो घञ्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_16_padarujavi_16"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "padarujaviSaspfSo GaY",
    text_dev              = "पदरुजविशस्पृशो घञ्",
    padaccheda_dev        = "पदरुज-विश-स्पृशः घञ्",
    why_dev               = "धातोः प्रत्ययः (३.3.16)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
