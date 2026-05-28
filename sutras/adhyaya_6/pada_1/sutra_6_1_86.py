"""
6.1.86  षत्वतुकोरसिद्धः  —  VIDHI

Padaccheda: षत्व-तुकोः असिद्धः

षत्वतुकोरसिद्धः (6.1.86)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_86_zatvatukor_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_86_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zatvatukorasidDaH",
    text_dev              = "षत्वतुकोरसिद्धः",
    padaccheda_dev        = "षत्व-तुकोः असिद्धः",
    why_dev               = "(सूत्रम् 6.1.86) षत्वतुकोरसिद्धः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
