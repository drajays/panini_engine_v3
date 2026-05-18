"""
4.1.154  तिकादिभ्यः फिञ्  —  VIDHI

Padaccheda: तिक-आदिभ्यः फिञ्

तिकादिभ्यः फिञ् (4.1.154)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_154_tikAdiByaH_154"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_154_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.154"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.154",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tikAdiByaH PiY",
    text_dev              = "तिकादिभ्यः फिञ्",
    padaccheda_dev        = "तिक-आदिभ्यः फिञ्",
    why_dev               = "(सूत्रम् 4.1.154) तिकादिभ्यः फिञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
