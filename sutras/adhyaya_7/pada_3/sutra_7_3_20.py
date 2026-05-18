"""
7.3.20  अनुशतिकादीनां च  —  VIDHI

Padaccheda: अनुशतिक-आदीनाम् च

अनुशतिकादीनां च (7.3.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_20_anuSatikAd_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_20_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anuSatikAdInAM ca",
    text_dev              = "अनुशतिकादीनां च",
    padaccheda_dev        = "अनुशतिक-आदीनाम् च",
    why_dev               = "(सूत्रम् 7.3.20) अनुशतिकादीनां च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
