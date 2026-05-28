"""
8.1.41  शेषे विभाषा  —  VIDHI

Padaccheda: शेषे विभाषा

शेषे विभाषा (8.1.41)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_41_Seze_41"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_41_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Seze viBAzA",
    text_dev              = "शेषे विभाषा",
    padaccheda_dev        = "शेषे विभाषा",
    why_dev               = "(सूत्रम् 8.1.41) शेषे विभाषा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
