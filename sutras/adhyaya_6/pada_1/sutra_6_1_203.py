"""
6.1.203  वृषादीनां च  —  VIDHI

Padaccheda: वृष-आदीनाम् च

वृषादीनां च (6.1.203)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_203_vfzAdInAM_203"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_203_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.203"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.203",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vfzAdInAM ca",
    text_dev              = "वृषादीनां च",
    padaccheda_dev        = "वृष-आदीनाम् च",
    why_dev               = "(सूत्रम् 6.1.203) वृषादीनां च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
