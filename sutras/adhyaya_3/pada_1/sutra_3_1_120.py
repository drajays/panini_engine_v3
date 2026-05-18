"""
3.1.120  विभाषा कृवृषोः  —  VIDHI

Padaccheda: विभाषा कृ-वृषोः

Krt suffix rule from dhatu: विभाषा कृवृषोः (120)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_120_viBAzA_120"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_120_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.120"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.120",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA kfvfzoH",
    text_dev              = "विभाषा कृवृषोः",
    padaccheda_dev        = "विभाषा कृ-वृषोः",
    why_dev               = "धातोः [विभाषा कृवृषोः]-प्रत्ययः विहितः (३.१.120)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
