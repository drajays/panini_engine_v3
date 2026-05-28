"""
8.4.10  वा भावकरणयोः  —  VIDHI

Padaccheda: वा भाव-करणयोः

वा भावकरणयोः (8.4.10)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_10_vA_10"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_10_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA BAvakaraRayoH",
    text_dev              = "वा भावकरणयोः",
    padaccheda_dev        = "वा भाव-करणयोः",
    why_dev               = "(सूत्रम् 8.4.10) वा भावकरणयोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
