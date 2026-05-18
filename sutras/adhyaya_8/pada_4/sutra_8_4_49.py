"""
8.4.49  शरोऽचि  —  VIDHI

Padaccheda: शरः अचि

शरोऽचि (8.4.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_49_Saroci_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_49_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Saro'ci",
    text_dev              = "शरोऽचि",
    padaccheda_dev        = "शरः अचि",
    why_dev               = "(सूत्रम् 8.4.49) शरोऽचि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
