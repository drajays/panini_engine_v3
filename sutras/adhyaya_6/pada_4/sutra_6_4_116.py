"""
6.4.116  जहातेश्च  —  VIDHI

Padaccheda: जहातेः च

जहातेश्च (6.4.116)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_116_jahAteSca_116"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.116", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jahAteSca",
    text_dev              = "जहातेश्च",
    padaccheda_dev        = "जहातेः च",
    why_dev               = "(सूत्रम् 6.4.116) जहातेश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
