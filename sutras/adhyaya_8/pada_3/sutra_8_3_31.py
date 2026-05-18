"""
8.3.31  शि तुक्  —  VIDHI

Padaccheda: शि तुक्

शि तुक् (8.3.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_31_Si_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Si tuk",
    text_dev              = "शि तुक्",
    padaccheda_dev        = "शि तुक्",
    why_dev               = "(सूत्रम् 8.3.31) शि तुक्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
