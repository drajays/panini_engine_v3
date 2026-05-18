"""
4.3.33  अणञौ च  —  VIDHI

Padaccheda: अण्-अञौ च

अणञौ च (4.3.33)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_33_aRaYO_33"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_33_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aRaYO ca",
    text_dev              = "अणञौ च",
    padaccheda_dev        = "अण्-अञौ च",
    why_dev               = "(सूत्रम् 4.3.33) अणञौ च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
