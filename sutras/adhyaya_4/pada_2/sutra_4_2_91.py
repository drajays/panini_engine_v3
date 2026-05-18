"""
4.2.91  नडादीनां कुक् च  —  VIDHI

Padaccheda: नड-आदीनाम् कुक् च

नडादीनां कुक् च (4.2.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_91_naqAdInAM_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_91_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naqAdInAM kuk ca",
    text_dev              = "नडादीनां कुक् च",
    padaccheda_dev        = "नड-आदीनाम् कुक् च",
    why_dev               = "(सूत्रम् 4.2.91) नडादीनां कुक् च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
