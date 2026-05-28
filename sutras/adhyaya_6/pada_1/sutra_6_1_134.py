"""
6.1.134  सोऽचि लोपे चेत् पादपूरणम्  —  VIDHI

Padaccheda: सः (षष्ठ्यर्थे प्रथमा) अचि लोपे चेत् पादपूरणम्

सोऽचि लोपे चेत् पादपूरणम् (6.1.134)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_134_soci_134"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.134"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.134",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "so'ci lope cet pAdapUraRam",
    text_dev              = "सोऽचि लोपे चेत् पादपूरणम्",
    padaccheda_dev        = "सः (षष्ठ्यर्थे प्रथमा) अचि लोपे चेत् पादपूरणम्",
    why_dev               = "(सूत्रम् 6.1.134) सोऽचि लोपे चेत् पादपूरणम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
