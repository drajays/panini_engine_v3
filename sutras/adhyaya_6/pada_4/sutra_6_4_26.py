"""
6.4.26  रञ्जेश्च  —  VIDHI

Padaccheda: रञ्जेः च

रञ्जेश्च (6.4.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_26_raYjeSca_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_26_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "raYjeSca",
    text_dev              = "रञ्जेश्च",
    padaccheda_dev        = "रञ्जेः च",
    why_dev               = "(सूत्रम् 6.4.26) रञ्जेश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
