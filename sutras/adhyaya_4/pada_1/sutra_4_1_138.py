"""
4.1.138  क्षत्राद्घः  —  VIDHI

Padaccheda: क्षत्रात् घः

क्षत्राद्घः (4.1.138)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_138_kzatrAdGaH_138"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_138_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.138"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzatrAdGaH",
    text_dev              = "क्षत्राद्घः",
    padaccheda_dev        = "क्षत्रात् घः",
    why_dev               = "(सूत्रम् 4.1.138) क्षत्राद्घः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
