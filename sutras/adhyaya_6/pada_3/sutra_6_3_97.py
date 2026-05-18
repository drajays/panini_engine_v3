"""
6.3.97  द्व्यन्तरुपसर्गेभ्योऽप ईत्  —  VIDHI

Padaccheda: द्वि-अन्तः-उपसर्गेभ्यः अपः ईत्

द्व्यन्तरुपसर्गेभ्योऽप ईत् (6.3.97)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_97_dvyantarup_97"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_97_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvyantarupasargeByo'pa It",
    text_dev              = "द्व्यन्तरुपसर्गेभ्योऽप ईत्",
    padaccheda_dev        = "द्वि-अन्तः-उपसर्गेभ्यः अपः ईत्",
    why_dev               = "(सूत्रम् 6.3.97) द्व्यन्तरुपसर्गेभ्योऽप ईत्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
