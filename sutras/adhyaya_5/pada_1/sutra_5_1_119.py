"""
5.1.119  तस्य भावस्त्वतलौ  —  VIDHI

Padaccheda: तस्य भावः त्व-तलौ

तस्य भावस्त्वतलौ (5.1.119)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_119_tasya_119"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_119_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasya BAvastvatalO",
    text_dev              = "तस्य भावस्त्वतलौ",
    padaccheda_dev        = "तस्य भावः त्व-तलौ",
    why_dev               = "(सूत्रम् 5.1.119) तस्य भावस्त्वतलौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
