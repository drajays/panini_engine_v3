"""
7.3.112  आण्नद्याः  —  VIDHI

Padaccheda: आट् नद्याः

आण्नद्याः (7.3.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_112_ARnadyAH_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_112_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ARnadyAH",
    text_dev              = "आण्नद्याः",
    padaccheda_dev        = "आट् नद्याः",
    why_dev               = "(सूत्रम् 7.3.112) आण्नद्याः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
