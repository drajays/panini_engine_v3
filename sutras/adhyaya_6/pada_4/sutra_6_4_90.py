"""
6.4.90  दोषो णौ  —  VIDHI

Padaccheda: दोषः णौ

दोषो णौ (6.4.90)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_90_dozo_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_90_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dozo RO",
    text_dev              = "दोषो णौ",
    padaccheda_dev        = "दोषः णौ",
    why_dev               = "(सूत्रम् 6.4.90) दोषो णौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
