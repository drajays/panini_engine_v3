"""
8.1.52  लोट् च  —  VIDHI

Padaccheda: लोट् च

लोट् च (8.1.52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_52_low_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_52_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "low ca",
    text_dev              = "लोट् च",
    padaccheda_dev        = "लोट् च",
    why_dev               = "(सूत्रम् 8.1.52) लोट् च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
