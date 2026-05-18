"""
4.1.170  द्व्यञ्मगधकलिङ्गसूरमसादण्  —  VIDHI

Padaccheda: द्वि-अच्-मगध-कलिङ्ग-सूरमसाद् अण्

द्व्यञ्मगधकलिङ्गसूरमसादण् (4.1.170)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_170_dvyaYmagaD_170"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_170_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.170"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.170",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvyaYmagaDakaliNgasUramasAdaR",
    text_dev              = "द्व्यञ्मगधकलिङ्गसूरमसादण्",
    padaccheda_dev        = "द्वि-अच्-मगध-कलिङ्ग-सूरमसाद् अण्",
    why_dev               = "(सूत्रम् 4.1.170) द्व्यञ्मगधकलिङ्गसूरमसादण्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
