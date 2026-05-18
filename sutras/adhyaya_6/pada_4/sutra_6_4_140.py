"""
6.4.140  आतो धातोः  —  VIDHI

Padaccheda: आतः धातोः

आतो धातोः (6.4.140)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_140_Ato_140"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_140_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.140"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.140",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ato DAtoH",
    text_dev              = "आतो धातोः",
    padaccheda_dev        = "आतः धातोः",
    why_dev               = "(सूत्रम् 6.4.140) आतो धातोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
