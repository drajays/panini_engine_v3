"""
6.3.65  इष्टकेषीकामालानां चिततूलभारिषु  —  VIDHI

Padaccheda: इष्टका-इषीका-मालानाम् चित-तूल-भारिषु

इष्टकेषीकामालानां चिततूलभारिषु (6.3.65)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_65_izwakezIkA_65"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_65_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "izwakezIkAmAlAnAM citatUlaBArizu",
    text_dev              = "इष्टकेषीकामालानां चिततूलभारिषु",
    padaccheda_dev        = "इष्टका-इषीका-मालानाम् चित-तूल-भारिषु",
    why_dev               = "(सूत्रम् 6.3.65) इष्टकेषीकामालानां चिततूलभारिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
