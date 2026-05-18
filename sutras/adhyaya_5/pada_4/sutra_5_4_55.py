"""
5.4.55  देये त्रा च  —  VIDHI

Padaccheda: देये त्रा च

देये त्रा च (5.4.55)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_55_deye_55"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_55_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "deye trA ca",
    text_dev              = "देये त्रा च",
    padaccheda_dev        = "देये त्रा च",
    why_dev               = "(सूत्रम् 5.4.55) देये त्रा च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
