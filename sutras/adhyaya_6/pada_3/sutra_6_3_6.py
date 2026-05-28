"""
6.3.6  आत्मनश्च पूरणे  —  VIDHI

Padaccheda: आत्मनः च पूरणे

आत्मनश्च पूरणे (6.3.6)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_6_AtmanaSca_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmanaSca pUraRe",
    text_dev              = "आत्मनश्च पूरणे",
    padaccheda_dev        = "आत्मनः च पूरणे",
    why_dev               = "(सूत्रम् 6.3.6) आत्मनश्च पूरणे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
