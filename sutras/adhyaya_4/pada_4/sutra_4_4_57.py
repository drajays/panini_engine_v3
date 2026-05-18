"""
4.4.57  प्रहरणम्  —  VIDHI

Padaccheda: प्रहरणम्

प्रहरणम् (4.4.57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_57_praharaRam_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_57_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "praharaRam",
    text_dev              = "प्रहरणम्",
    padaccheda_dev        = "प्रहरणम्",
    why_dev               = "(सूत्रम् 4.4.57) प्रहरणम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
