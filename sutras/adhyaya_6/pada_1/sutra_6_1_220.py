"""
6.1.220  अन्तोऽवत्याः  —  VIDHI

Padaccheda: अन्तः अवत्याः

अन्तोऽवत्याः (6.1.220)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_220_antovatyA_220"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_220_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.220"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.220",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anto'vatyAH",
    text_dev              = "अन्तोऽवत्याः",
    padaccheda_dev        = "अन्तः अवत्याः",
    why_dev               = "(सूत्रम् 6.1.220) अन्तोऽवत्याः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
