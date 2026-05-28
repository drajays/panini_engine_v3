"""
7.3.4  द्वारादीनां च  —  VIDHI

Padaccheda: द्वार-आदीनाम् च

द्वारादीनां च (7.3.4)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_4_dvArAdInAM_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.4", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_3_4_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvArAdInAM ca",
    text_dev              = "द्वारादीनां च",
    padaccheda_dev        = "द्वार-आदीनाम् च",
    why_dev               = "(सूत्रम् 7.3.4) द्वारादीनां च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
