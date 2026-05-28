"""
6.4.164  इनण्यनपत्ये  —  VIDHI

Padaccheda: इन् अणि अन्-अपत्ये

इनण्यनपत्ये (6.4.164)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_164_inaRyanapa_164"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.164", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.164"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.164",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "inaRyanapatye",
    text_dev              = "इनण्यनपत्ये",
    padaccheda_dev        = "इन् अणि अन्-अपत्ये",
    why_dev               = "(सूत्रम् 6.4.164) इनण्यनपत्ये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
