"""
8.2.58  वित्तो भोगप्रत्यययोः  —  VIDHI

Padaccheda: वित्तः भोगप्रत्यययोः

वित्तो भोगप्रत्यययोः (8.2.58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_58_vitto_58"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_58_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vitto BogapratyayayoH",
    text_dev              = "वित्तो भोगप्रत्यययोः",
    padaccheda_dev        = "वित्तः भोगप्रत्यययोः",
    why_dev               = "(सूत्रम् 8.2.58) वित्तो भोगप्रत्यययोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
