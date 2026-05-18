"""
4.2.87  कुमुदनडवेतसेभ्यो ड्मतुप्  —  VIDHI

Padaccheda: कुमुद-नड-वेतसेभ्यः ड्‍मतुप्

कुमुदनडवेतसेभ्यो ड्मतुप् (4.2.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_87_kumudanaqa_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_87_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kumudanaqavetaseByo qmatup",
    text_dev              = "कुमुदनडवेतसेभ्यो ड्मतुप्",
    padaccheda_dev        = "कुमुद-नड-वेतसेभ्यः ड्‍मतुप्",
    why_dev               = "(सूत्रम् 4.2.87) कुमुदनडवेतसेभ्यो ड्मतुप्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
