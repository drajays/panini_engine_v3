"""
6.3.86  चरणे ब्रह्मचारिणि  —  VIDHI

Padaccheda: चरणे ब्रह्मचारिणि

चरणे ब्रह्मचारिणि (6.3.86)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_86_caraRe_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_86_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "caraRe brahmacAriRi",
    text_dev              = "चरणे ब्रह्मचारिणि",
    padaccheda_dev        = "चरणे ब्रह्मचारिणि",
    why_dev               = "(सूत्रम् 6.3.86) चरणे ब्रह्मचारिणि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
