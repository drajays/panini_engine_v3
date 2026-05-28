"""
8.3.33  मय उञो वो वा  —  VIDHI

Padaccheda: मयः उञो वः वा

मय उञो वो वा (8.3.33)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_33_maya_33"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "maya uYo vo vA",
    text_dev              = "मय उञो वो वा",
    padaccheda_dev        = "मयः उञो वः वा",
    why_dev               = "(सूत्रम् 8.3.33) मय उञो वो वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
