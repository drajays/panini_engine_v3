"""
6.4.141  मन्त्रेष्वाङ्यादेरात्मनः  —  VIDHI

Padaccheda: मन्त्रेषु आङि आदेः आत्मनः

मन्त्रेष्वाङ्यादेरात्मनः (6.4.141)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_141_mantrezvAN_141"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.141", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.141"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.141",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mantrezvANyAderAtmanaH",
    text_dev              = "मन्त्रेष्वाङ्यादेरात्मनः",
    padaccheda_dev        = "मन्त्रेषु आङि आदेः आत्मनः",
    why_dev               = "(सूत्रम् 6.4.141) मन्त्रेष्वाङ्यादेरात्मनः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
