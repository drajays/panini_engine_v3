"""
5.4.69  न पूजनात्  —  VIDHI

Padaccheda: न पूजनात्

न पूजनात् (5.4.69)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_69_na_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_69_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na pUjanAt",
    text_dev              = "न पूजनात्",
    padaccheda_dev        = "न पूजनात्",
    why_dev               = "(सूत्रम् 5.4.69) न पूजनात्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
