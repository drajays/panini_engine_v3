"""
3.1.143  विभाषा ग्रहेः  —  VIDHI

Padaccheda: विभाषा ग्रहः

Krt suffix rule from dhatu: विभाषा ग्रहेः (143)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_143_viBAzA_143"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_143_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.143"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.143",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA graheH",
    text_dev              = "विभाषा ग्रहेः",
    padaccheda_dev        = "विभाषा ग्रहः",
    why_dev               = "धातोः [विभाषा ग्रहेः]-प्रत्ययः विहितः (३.१.143)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
