"""
6.2.20  वा भुवनम्  —  VIDHI

Padaccheda: वा भुवनम्

वा भुवनम् (6.2.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_20_vA_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_20_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA Buvanam",
    text_dev              = "वा भुवनम्",
    padaccheda_dev        = "वा भुवनम्",
    why_dev               = "(सूत्रम् 6.2.20) वा भुवनम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
