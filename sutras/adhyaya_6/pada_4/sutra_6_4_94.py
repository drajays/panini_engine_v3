"""
6.4.94  खचि ह्रस्वः  —  VIDHI

Padaccheda: खचि ह्रस्वः

खचि ह्रस्वः (6.4.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_94_Kaci_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Kaci hrasvaH",
    text_dev              = "खचि ह्रस्वः",
    padaccheda_dev        = "खचि ह्रस्वः",
    why_dev               = "(सूत्रम् 6.4.94) खचि ह्रस्वः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
