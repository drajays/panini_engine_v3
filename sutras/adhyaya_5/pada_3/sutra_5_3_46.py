"""
5.3.46  एधाच्च  —  VIDHI

Padaccheda: एधाच् च

एधाच्च (5.3.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_46_eDAcca_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_46_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "eDAcca",
    text_dev              = "एधाच्च",
    padaccheda_dev        = "एधाच् च",
    why_dev               = "(सूत्रम् 5.3.46) एधाच्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
