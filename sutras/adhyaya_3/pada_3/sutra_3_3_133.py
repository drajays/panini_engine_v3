"""
3.3.133  क्षिप्रवचने लृट्  —  VIDHI

Padaccheda: क्षिप्रवचने लृट्

krt-suffix rule: क्षिप्रवचने लृट्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_133_kzipravaca_133"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_133_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.133"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.133",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzipravacane lfw",
    text_dev              = "क्षिप्रवचने लृट्",
    padaccheda_dev        = "क्षिप्रवचने लृट्",
    why_dev               = "धातोः प्रत्ययः (३.3.133)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
