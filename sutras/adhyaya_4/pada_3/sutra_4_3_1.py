"""
4.3.1  युष्मदस्मदोरन्यतरस्यां खञ् च  —  VIDHI

Padaccheda: युष्मद्-अस्मदोः अन्यतरस्याम् खञ् च

युष्मदस्मदोरन्यतरस्यां खञ् च (4.3.1)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_1_yuzmadasma_1"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_1_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.1"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.1",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yuzmadasmadoranyatarasyAM KaY ca",
    text_dev              = "युष्मदस्मदोरन्यतरस्यां खञ् च",
    padaccheda_dev        = "युष्मद्-अस्मदोः अन्यतरस्याम् खञ् च",
    why_dev               = "(सूत्रम् 4.3.1) युष्मदस्मदोरन्यतरस्यां खञ् च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
