"""
3.2.32  वहाभ्रे लिहः  —  VIDHI

Padaccheda: वह-अभ्रे लिहः

krt-suffix rule: वहाभ्रे लिहः (32)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_32_vahABre_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_32_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vahABre lihaH",
    text_dev              = "वहाभ्रे लिहः",
    padaccheda_dev        = "वह-अभ्रे लिहः",
    why_dev               = "धातोः कृत्-प्रत्ययः [वहाभ्रे लिहः] विहितः (३.२.32)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
