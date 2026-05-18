"""
6.2.147  प्रवृद्धादीनां च  —  VIDHI

Padaccheda: प्रवृद्ध-आदीनाम् च

प्रवृद्धादीनां च (6.2.147)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_147_pravfdDAdI_147"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_147_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.147"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.147",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pravfdDAdInAM ca",
    text_dev              = "प्रवृद्धादीनां च",
    padaccheda_dev        = "प्रवृद्ध-आदीनाम् च",
    why_dev               = "(सूत्रम् 6.2.147) प्रवृद्धादीनां च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
