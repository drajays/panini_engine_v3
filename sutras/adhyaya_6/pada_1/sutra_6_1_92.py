"""
6.1.92  वा सुप्यापिशलेः  —  VIDHI

Padaccheda: वा सुपि आपिशलेः

वा सुप्यापिशलेः (6.1.92)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_92_vA_92"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_92_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.92"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA supyApiSaleH",
    text_dev              = "वा सुप्यापिशलेः",
    padaccheda_dev        = "वा सुपि आपिशलेः",
    why_dev               = "(सूत्रम् 6.1.92) वा सुप्यापिशलेः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
