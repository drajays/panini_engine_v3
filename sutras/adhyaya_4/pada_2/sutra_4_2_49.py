"""
4.2.49  पाशादिभ्यो यः  —  VIDHI

Padaccheda: पाश-आदिभ्यः यः

पाशादिभ्यो यः (4.2.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_49_pASAdiByo_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_49_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pASAdiByo yaH",
    text_dev              = "पाशादिभ्यो यः",
    padaccheda_dev        = "पाश-आदिभ्यः यः",
    why_dev               = "(सूत्रम् 4.2.49) पाशादिभ्यो यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
