"""
4.2.74  उदक् च विपाशः  —  VIDHI

Padaccheda: उदक् च विपाशः

उदक् च विपाशः (4.2.74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_74_udak_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_74_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udak ca vipASaH",
    text_dev              = "उदक् च विपाशः",
    padaccheda_dev        = "उदक् च विपाशः",
    why_dev               = "(सूत्रम् 4.2.74) उदक् च विपाशः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
