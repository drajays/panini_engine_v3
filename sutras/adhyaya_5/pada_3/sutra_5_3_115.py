"""
5.3.115  वृकाट्टेण्यण्  —  VIDHI

Padaccheda: वृकात् टेण्यण्

वृकाट्टेण्यण् (5.3.115)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_115_vfkAwweRya_115"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_115_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vfkAwweRyaR",
    text_dev              = "वृकाट्टेण्यण्",
    padaccheda_dev        = "वृकात् टेण्यण्",
    why_dev               = "(सूत्रम् 5.3.115) वृकाट्टेण्यण्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
