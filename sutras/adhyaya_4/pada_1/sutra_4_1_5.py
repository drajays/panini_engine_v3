"""
4.1.5  ऋन्नेभ्यो ङीप्  —  VIDHI

Padaccheda: ऋत्-नेभ्यः ङीप्

ऋन्नेभ्यो ङीप् (4.1.5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_5_fnneByo_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_5_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fnneByo NIp",
    text_dev              = "ऋन्नेभ्यो ङीप्",
    padaccheda_dev        = "ऋत्-नेभ्यः ङीप्",
    why_dev               = "(सूत्रम् 4.1.5) ऋन्नेभ्यो ङीप्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
