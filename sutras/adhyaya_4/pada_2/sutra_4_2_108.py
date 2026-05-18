"""
4.2.108  मद्रेभ्योऽञ्  —  VIDHI

Padaccheda: मद्रेभ्यः अञ्

मद्रेभ्योऽञ् (4.2.108)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_108_madreByoY_108"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_108_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "madreByo'Y",
    text_dev              = "मद्रेभ्योऽञ्",
    padaccheda_dev        = "मद्रेभ्यः अञ्",
    why_dev               = "(सूत्रम् 4.2.108) मद्रेभ्योऽञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
