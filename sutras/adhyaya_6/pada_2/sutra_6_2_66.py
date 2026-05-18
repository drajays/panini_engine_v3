"""
6.2.66  युक्ते च  —  VIDHI

Padaccheda: युक्ते च

युक्ते च (6.2.66)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_66_yukte_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_66_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yukte ca",
    text_dev              = "युक्ते च",
    padaccheda_dev        = "युक्ते च",
    why_dev               = "(सूत्रम् 6.2.66) युक्ते च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
