"""
6.4.35  शा हौ  —  VIDHI

Padaccheda: शा हौ

शा हौ (6.4.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_35_SA_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_35_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SA hO",
    text_dev              = "शा हौ",
    padaccheda_dev        = "शा हौ",
    why_dev               = "(सूत्रम् 6.4.35) शा हौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
