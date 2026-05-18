"""
6.3.24  विभाषा स्वसृपत्योः  —  VIDHI

Padaccheda: विभाषा स्वसृ-पत्योः

विभाषा स्वसृपत्योः (6.3.24)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_24_viBAzA_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_24_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA svasfpatyoH",
    text_dev              = "विभाषा स्वसृपत्योः",
    padaccheda_dev        = "विभाषा स्वसृ-पत्योः",
    why_dev               = "(सूत्रम् 6.3.24) विभाषा स्वसृपत्योः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
