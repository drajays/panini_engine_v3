"""
5.1.42  तस्येश्वरः  —  VIDHI

Padaccheda: तस्य ईश्वरः

तस्येश्वरः (5.1.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_42_tasyeSvara_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_42_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasyeSvaraH",
    text_dev              = "तस्येश्वरः",
    padaccheda_dev        = "तस्य ईश्वरः",
    why_dev               = "(सूत्रम् 5.1.42) तस्येश्वरः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
