"""
6.3.134  इकः सुञि  —  VIDHI

Padaccheda: इकः सुञि

इकः सुञि (6.3.134)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_134_ikaH_134"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_134_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.134"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.134",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ikaH suYi",
    text_dev              = "इकः सुञि",
    padaccheda_dev        = "इकः सुञि",
    why_dev               = "(सूत्रम् 6.3.134) इकः सुञि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
