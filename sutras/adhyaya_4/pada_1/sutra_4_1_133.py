"""
4.1.133  ढकि लोपः  —  VIDHI

Padaccheda: ढकि लोपः

ढकि लोपः (4.1.133)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_133_Qaki_133"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_133_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.133"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.133",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Qaki lopaH",
    text_dev              = "ढकि लोपः",
    padaccheda_dev        = "ढकि लोपः",
    why_dev               = "(सूत्रम् 4.1.133) ढकि लोपः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
