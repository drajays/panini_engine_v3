"""
7.1.67  उपसर्गात् खल्घञोः  —  VIDHI

Padaccheda: उपसर्गात् खल्-घञोः

उपसर्गात् खल्घञोः (7.1.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_67_upasargAt_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_67_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargAt KalGaYoH",
    text_dev              = "उपसर्गात् खल्घञोः",
    padaccheda_dev        = "उपसर्गात् खल्-घञोः",
    why_dev               = "(सूत्रम् 7.1.67) उपसर्गात् खल्घञोः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
