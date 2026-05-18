"""
7.4.21  शीङः सार्वधातुके गुणः  —  VIDHI

Padaccheda: शीङः सार्वधातुके गुणः

शीङः सार्वधातुके गुणः (7.4.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_21_SINaH_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_21_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SINaH sArvaDAtuke guRaH",
    text_dev              = "शीङः सार्वधातुके गुणः",
    padaccheda_dev        = "शीङः सार्वधातुके गुणः",
    why_dev               = "(सूत्रम् 7.4.21) शीङः सार्वधातुके गुणः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
