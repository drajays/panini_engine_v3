"""
7.1.96  स्त्रियां च  —  VIDHI

Padaccheda: स्त्रियाम् च

स्त्रियां च (7.1.96)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_96_striyAM_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_96_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "striyAM ca",
    text_dev              = "स्त्रियां च",
    padaccheda_dev        = "स्त्रियाम् च",
    why_dev               = "(सूत्रम् 7.1.96) स्त्रियां च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
