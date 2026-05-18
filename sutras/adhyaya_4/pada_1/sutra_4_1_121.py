"""
4.1.121  द्व्यचः  —  VIDHI

Padaccheda: द्वि-अचः

द्व्यचः (4.1.121)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_121_dvyacaH_121"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_121_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvyacaH",
    text_dev              = "द्व्यचः",
    padaccheda_dev        = "द्वि-अचः",
    why_dev               = "(सूत्रम् 4.1.121) द्व्यचः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
