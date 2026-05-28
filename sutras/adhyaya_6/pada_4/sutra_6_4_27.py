"""
6.4.27  घञि च भावकरणयोः  —  VIDHI

Padaccheda: घञि च भाव-करणयोः

घञि च भावकरणयोः (6.4.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_27_GaYi_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.27", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "GaYi ca BAvakaraRayoH",
    text_dev              = "घञि च भावकरणयोः",
    padaccheda_dev        = "घञि च भाव-करणयोः",
    why_dev               = "(सूत्रम् 6.4.27) घञि च भावकरणयोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
