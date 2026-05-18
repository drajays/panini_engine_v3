"""
4.2.51  इनित्रकट्यचश्च  —  VIDHI

Padaccheda: इनि-त्र-कट्यचः च

इनित्रकट्यचश्च (4.2.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_51_initrakawy_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_51_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "initrakawyacaSca",
    text_dev              = "इनित्रकट्यचश्च",
    padaccheda_dev        = "इनि-त्र-कट्यचः च",
    why_dev               = "(सूत्रम् 4.2.51) इनित्रकट्यचश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
