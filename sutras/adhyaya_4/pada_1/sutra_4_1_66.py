"""
4.1.66  ऊङुतः  —  VIDHI

Padaccheda: ऊङ् उतः

ऊङुतः (4.1.66)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_66_UNutaH_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_66_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UNutaH",
    text_dev              = "ऊङुतः",
    padaccheda_dev        = "ऊङ् उतः",
    why_dev               = "(सूत्रम् 4.1.66) ऊङुतः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
