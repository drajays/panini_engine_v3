"""
8.1.58  चादिषु च  —  VIDHI

Padaccheda: च-आदिषु च

चादिषु च (8.1.58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_58_cAdizu_58"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_58_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cAdizu ca",
    text_dev              = "चादिषु च",
    padaccheda_dev        = "च-आदिषु च",
    why_dev               = "(सूत्रम् 8.1.58) चादिषु च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
