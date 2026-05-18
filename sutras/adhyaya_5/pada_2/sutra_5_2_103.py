"""
5.2.103  अण् च  —  VIDHI

Padaccheda: अण् च

अण् च (5.2.103)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_103_aR_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_103_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aR ca",
    text_dev              = "अण् च",
    padaccheda_dev        = "अण् च",
    why_dev               = "(सूत्रम् 5.2.103) अण् च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
