"""
5.4.122  नित्यमसिच् प्रजामेधयोः  —  VIDHI

Padaccheda: नित्यम् असिच् प्रजा-मेधयोः

नित्यमसिच् प्रजामेधयोः (5.4.122)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_122_nityamasic_122"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_122_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityamasic prajAmeDayoH",
    text_dev              = "नित्यमसिच् प्रजामेधयोः",
    padaccheda_dev        = "नित्यम् असिच् प्रजा-मेधयोः",
    why_dev               = "(सूत्रम् 5.4.122) नित्यमसिच् प्रजामेधयोः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
