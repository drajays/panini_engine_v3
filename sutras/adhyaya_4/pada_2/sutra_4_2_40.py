"""
4.2.40  केदाराद्यञ् च  —  VIDHI

Padaccheda: केदारात् यञ् च

केदाराद्यञ् च (4.2.40)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_40_kedArAdyaY_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_40_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kedArAdyaY ca",
    text_dev              = "केदाराद्यञ् च",
    padaccheda_dev        = "केदारात् यञ् च",
    why_dev               = "(सूत्रम् 4.2.40) केदाराद्यञ् च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
