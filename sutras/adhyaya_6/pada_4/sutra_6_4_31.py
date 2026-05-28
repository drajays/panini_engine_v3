"""
6.4.31  क्त्वि स्कन्दिस्यन्दोः  —  VIDHI

Padaccheda: क्त्वि स्कन्दि-स्यन्दोः

क्त्वि स्कन्दिस्यन्दोः (6.4.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_31_ktvi_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.31", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ktvi skandisyandoH",
    text_dev              = "क्त्वि स्कन्दिस्यन्दोः",
    padaccheda_dev        = "क्त्वि स्कन्दि-स्यन्दोः",
    why_dev               = "(सूत्रम् 6.4.31) क्त्वि स्कन्दिस्यन्दोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
