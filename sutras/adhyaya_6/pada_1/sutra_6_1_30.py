"""
6.1.30  विभाषा श्वेः  —  VIDHI

Padaccheda: विभाषा श्वेः

विभाषा श्वेः (6.1.30)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_30_viBAzA_30"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_30_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA SveH",
    text_dev              = "विभाषा श्वेः",
    padaccheda_dev        = "विभाषा श्वेः",
    why_dev               = "(सूत्रम् 6.1.30) विभाषा श्वेः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
