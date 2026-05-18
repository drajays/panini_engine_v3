"""
5.1.80  तमधीष्टो भृतो भूतो भावी  —  VIDHI

Padaccheda: तम् अधीष्टः भृतः भूतः भावी

तमधीष्टो भृतो भूतो भावी (5.1.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_80_tamaDIzwo_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_80_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tamaDIzwo Bfto BUto BAvI",
    text_dev              = "तमधीष्टो भृतो भूतो भावी",
    padaccheda_dev        = "तम् अधीष्टः भृतः भूतः भावी",
    why_dev               = "(सूत्रम् 5.1.80) तमधीष्टो भृतो भूतो भावी।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
