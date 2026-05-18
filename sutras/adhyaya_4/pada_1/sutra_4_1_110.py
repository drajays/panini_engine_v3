"""
4.1.110  अश्वादिभ्यः फञ्  —  VIDHI

Padaccheda: अश्व-आदिभ्यः फञ्

अश्वादिभ्यः फञ् (4.1.110)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_110_aSvAdiByaH_110"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_110_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aSvAdiByaH PaY",
    text_dev              = "अश्वादिभ्यः फञ्",
    padaccheda_dev        = "अश्व-आदिभ्यः फञ्",
    why_dev               = "(सूत्रम् 4.1.110) अश्वादिभ्यः फञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
