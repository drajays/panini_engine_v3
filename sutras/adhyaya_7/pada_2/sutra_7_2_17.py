"""
7.2.17  विभाषा भावादिकर्मणोः  —  VIDHI

Padaccheda: विभाषा भाव-आदिकर्मणोः

विभाषा भावादिकर्मणोः (7.2.17)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_17_viBAzA_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.17", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_2_17_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA BAvAdikarmaRoH",
    text_dev              = "विभाषा भावादिकर्मणोः",
    padaccheda_dev        = "विभाषा भाव-आदिकर्मणोः",
    why_dev               = "(सूत्रम् 7.2.17) विभाषा भावादिकर्मणोः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
