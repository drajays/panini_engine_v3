"""
7.1.5  आत्मनेपदेष्वनतः  —  VIDHI

Padaccheda: आत्मनेपदेषु अन्-अतः

आत्मनेपदेष्वनतः (7.1.5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_5_Atmanepade_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_5_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmanepadezvanataH",
    text_dev              = "आत्मनेपदेष्वनतः",
    padaccheda_dev        = "आत्मनेपदेषु अन्-अतः",
    why_dev               = "(सूत्रम् 7.1.5) आत्मनेपदेष्वनतः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
