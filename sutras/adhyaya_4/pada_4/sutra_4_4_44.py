"""
4.4.44  परिषदो ण्यः  —  VIDHI

Padaccheda: परिषदः ण्यः

परिषदो ण्यः (4.4.44)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_44_parizado_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_44_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parizado RyaH",
    text_dev              = "परिषदो ण्यः",
    padaccheda_dev        = "परिषदः ण्यः",
    why_dev               = "(सूत्रम् 4.4.44) परिषदो ण्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
