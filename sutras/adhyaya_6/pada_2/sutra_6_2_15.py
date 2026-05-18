"""
6.2.15  सुखप्रिययोर्हिते  —  VIDHI

Padaccheda: सुख-प्रिययोः हिते

सुखप्रिययोर्हिते (6.2.15)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_15_suKapriyay_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_15_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suKapriyayorhite",
    text_dev              = "सुखप्रिययोर्हिते",
    padaccheda_dev        = "सुख-प्रिययोः हिते",
    why_dev               = "(सूत्रम् 6.2.15) सुखप्रिययोर्हिते।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
