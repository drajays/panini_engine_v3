"""
5.1.117  तदर्हम्  —  VIDHI

Padaccheda: तत् अर्हम्

तदर्हम् (5.1.117)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_117_tadarham_117"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_117_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadarham",
    text_dev              = "तदर्हम्",
    padaccheda_dev        = "तत् अर्हम्",
    why_dev               = "(सूत्रम् 5.1.117) तदर्हम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
