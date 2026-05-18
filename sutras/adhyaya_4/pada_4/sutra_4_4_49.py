"""
4.4.49  ऋतोऽञ्  —  VIDHI

Padaccheda: ऋतः अञ्

ऋतोऽञ् (4.4.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_49_ftoY_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_49_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fto'Y",
    text_dev              = "ऋतोऽञ्",
    padaccheda_dev        = "ऋतः अञ्",
    why_dev               = "(सूत्रम् 4.4.49) ऋतोऽञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
