"""
7.1.98  चतुरनडुहोरामुदात्तः  —  VIDHI

Padaccheda: चतुर्-अनडुहोः आम् उदात्तः

चतुरनडुहोरामुदात्तः (7.1.98)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_98_caturanaqu_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_98_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "caturanaquhorAmudAttaH",
    text_dev              = "चतुरनडुहोरामुदात्तः",
    padaccheda_dev        = "चतुर्-अनडुहोः आम् उदात्तः",
    why_dev               = "(सूत्रम् 7.1.98) चतुरनडुहोरामुदात्तः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
