"""
3.1.106  वदः सुपि क्यप् च  —  VIDHI

Padaccheda: वदः सुपि क्यप् च

Krt suffix rule from dhatu: वदः सुपि क्यप् च (106)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_106_vadaH_106"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_106_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.106"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.106",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vadaH supi kyap ca",
    text_dev              = "वदः सुपि क्यप् च",
    padaccheda_dev        = "वदः सुपि क्यप् च",
    why_dev               = "धातोः [वदः सुपि क्यप् च]-प्रत्ययः विहितः (३.१.106)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
