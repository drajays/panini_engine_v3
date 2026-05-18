"""
6.4.83  ओः सुपि  —  VIDHI

Padaccheda: ओः सुपि

ओः सुपि (6.4.83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_83_oH_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_83_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "oH supi",
    text_dev              = "ओः सुपि",
    padaccheda_dev        = "ओः सुपि",
    why_dev               = "(सूत्रम् 6.4.83) ओः सुपि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
