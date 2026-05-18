"""
5.4.150  सुहृद्दुर्हृदौ मित्रामित्रयोः  —  VIDHI

Padaccheda: सुहृद्-दुर्हृदौ मित्र-अमित्रयोः

सुहृद्दुर्हृदौ मित्रामित्रयोः (5.4.150)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_150_suhfddurhf_150"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_150_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.150"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.150",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suhfddurhfdO mitrAmitrayoH",
    text_dev              = "सुहृद्दुर्हृदौ मित्रामित्रयोः",
    padaccheda_dev        = "सुहृद्-दुर्हृदौ मित्र-अमित्रयोः",
    why_dev               = "(सूत्रम् 5.4.150) सुहृद्दुर्हृदौ मित्रामित्रयोः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
