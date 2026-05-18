"""
5.3.32  पश्चात्  —  VIDHI

Padaccheda: पश्चात्

पश्चात् (5.3.32)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_32_paScAt_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_32_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paScAt",
    text_dev              = "पश्चात्",
    padaccheda_dev        = "पश्चात्",
    why_dev               = "(सूत्रम् 5.3.32) पश्चात्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
