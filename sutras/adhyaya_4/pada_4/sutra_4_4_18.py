"""
4.4.18  अण् कुटिलिकायाः  —  VIDHI

Padaccheda: अण् कुटिलिकायाः

अण् कुटिलिकायाः (4.4.18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_18_aR_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_18_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aR kuwilikAyAH",
    text_dev              = "अण् कुटिलिकायाः",
    padaccheda_dev        = "अण् कुटिलिकायाः",
    why_dev               = "(सूत्रम् 4.4.18) अण् कुटिलिकायाः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
