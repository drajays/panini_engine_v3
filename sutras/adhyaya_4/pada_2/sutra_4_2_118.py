"""
4.2.118  विभाषोशीनरेषु  —  VIDHI

Padaccheda: विभाषा उशीनरेषु

विभाषोशीनरेषु (4.2.118)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_118_viBAzoSIna_118"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_118_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.118"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.118",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzoSInarezu",
    text_dev              = "विभाषोशीनरेषु",
    padaccheda_dev        = "विभाषा उशीनरेषु",
    why_dev               = "(सूत्रम् 4.2.118) विभाषोशीनरेषु।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
