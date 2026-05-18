"""
5.1.108  प्रकृष्टे ठञ्  —  VIDHI

Padaccheda: प्रकृष्टे ठञ्

प्रकृष्टे ठञ् (5.1.108)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_108_prakfzwe_108"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_108_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prakfzwe WaY",
    text_dev              = "प्रकृष्टे ठञ्",
    padaccheda_dev        = "प्रकृष्टे ठञ्",
    why_dev               = "(सूत्रम् 5.1.108) प्रकृष्टे ठञ्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
