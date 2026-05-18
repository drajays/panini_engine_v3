"""
6.1.183  दिवो झल्  —  VIDHI

Padaccheda: दिवः झल्

दिवो झल् (6.1.183)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_183_divo_183"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_183_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.183"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.183",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "divo Jal",
    text_dev              = "दिवो झल्",
    padaccheda_dev        = "दिवः झल्",
    why_dev               = "(सूत्रम् 6.1.183) दिवो झल्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
