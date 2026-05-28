"""
8.1.45  लोपे विभाषा  —  VIDHI

Padaccheda: लोपे विभाषा

लोपे विभाषा (8.1.45)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_45_lope_45"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_45_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lope viBAzA",
    text_dev              = "लोपे विभाषा",
    padaccheda_dev        = "लोपे विभाषा",
    why_dev               = "(सूत्रम् 8.1.45) लोपे विभाषा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
