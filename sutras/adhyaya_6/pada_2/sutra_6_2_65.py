"""
6.2.65  सप्तमीहारिणौ धर्म्येऽहरणे  —  VIDHI

Padaccheda: सप्तमी-हारिणौ धर्म्ये अहरणे

सप्तमीहारिणौ धर्म्येऽहरणे (6.2.65)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_65_saptamIhAr_65"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saptamIhAriRO Darmye'haraRe",
    text_dev              = "सप्तमीहारिणौ धर्म्येऽहरणे",
    padaccheda_dev        = "सप्तमी-हारिणौ धर्म्ये अहरणे",
    why_dev               = "(सूत्रम् 6.2.65) सप्तमीहारिणौ धर्म्येऽहरणे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
