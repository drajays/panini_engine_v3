"""
6.3.98  ऊदनोर्देशे  —  VIDHI

Padaccheda: ऊत् अनोः देशे

ऊदनोर्देशे (6.3.98)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_98_UdanordeSe_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_98_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UdanordeSe",
    text_dev              = "ऊदनोर्देशे",
    padaccheda_dev        = "ऊत् अनोः देशे",
    why_dev               = "(सूत्रम् 6.3.98) ऊदनोर्देशे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
