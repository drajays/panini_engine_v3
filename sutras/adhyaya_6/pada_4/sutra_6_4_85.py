"""
6.4.85  न भूसुधियोः  —  VIDHI

Padaccheda: न भू-सुधियोः

न भूसुधियोः (6.4.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_85_na_85"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.85", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na BUsuDiyoH",
    text_dev              = "न भूसुधियोः",
    padaccheda_dev        = "न भू-सुधियोः",
    why_dev               = "(सूत्रम् 6.4.85) न भूसुधियोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
