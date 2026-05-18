"""
6.2.60  षष्ठी प्रत्येनसि  —  VIDHI

Padaccheda: षष्ठी प्रत्येनसि

षष्ठी प्रत्येनसि (6.2.60)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_60_zazWI_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_60_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zazWI pratyenasi",
    text_dev              = "षष्ठी प्रत्येनसि",
    padaccheda_dev        = "षष्ठी प्रत्येनसि",
    why_dev               = "(सूत्रम् 6.2.60) षष्ठी प्रत्येनसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
