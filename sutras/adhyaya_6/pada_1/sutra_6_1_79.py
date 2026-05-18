"""
6.1.79  वान्तो यि प्रत्यये  —  VIDHI

Padaccheda: वान्तः यि प्रत्यये

वान्तो यि प्रत्यये (6.1.79)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_79_vAnto_79"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_79_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.79"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.79",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAnto yi pratyaye",
    text_dev              = "वान्तो यि प्रत्यये",
    padaccheda_dev        = "वान्तः यि प्रत्यये",
    why_dev               = "(सूत्रम् 6.1.79) वान्तो यि प्रत्यये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
