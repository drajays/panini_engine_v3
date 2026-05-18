"""
2.4.52  अस्तेर्भूः  —  VIDHI

Padaccheda: अस्तेः भूः

as root is replaced by bhu.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_52_asteh_bhuh"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_52_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asterBUH",
    text_dev              = "अस्तेर्भूः",
    padaccheda_dev        = "अस्तेः भूः",
    why_dev               = "अस्तेः भूः (२.४.५२)।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
