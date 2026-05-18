"""
7.1.81  शप्श्यनोर्नित्यम्  —  VIDHI

Padaccheda: शप्-श्यनोः नित्यम्

शप्श्यनोर्नित्यम् (7.1.81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_81_SapSyanorn_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_81_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SapSyanornityam",
    text_dev              = "शप्श्यनोर्नित्यम्",
    padaccheda_dev        = "शप्-श्यनोः नित्यम्",
    why_dev               = "(सूत्रम् 7.1.81) शप्श्यनोर्नित्यम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
