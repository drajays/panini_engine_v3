"""
3.2.4  सुपि स्थः  —  VIDHI

Padaccheda: सुपि स्थः

krt-suffix rule: सुपि स्थः (4)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_4_supi_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_4_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "supi sTaH",
    text_dev              = "सुपि स्थः",
    padaccheda_dev        = "सुपि स्थः",
    why_dev               = "धातोः कृत्-प्रत्ययः [सुपि स्थः] विहितः (३.२.4)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
