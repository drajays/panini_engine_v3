"""
7.3.88  भूसुवोस्तिङि  —  VIDHI

Padaccheda: भू-सुवोः तिङि

भूसुवोस्तिङि (7.3.88)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_88_BUsuvostiN_88"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_88_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BUsuvostiNi",
    text_dev              = "भूसुवोस्तिङि",
    padaccheda_dev        = "भू-सुवोः तिङि",
    why_dev               = "(सूत्रम् 7.3.88) भूसुवोस्तिङि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
