"""
6.2.95  कुमार्यां वयसि  —  VIDHI

Padaccheda: कुमार्याम् वयसि

कुमार्यां वयसि (6.2.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_95_kumAryAM_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kumAryAM vayasi",
    text_dev              = "कुमार्यां वयसि",
    padaccheda_dev        = "कुमार्याम् वयसि",
    why_dev               = "(सूत्रम् 6.2.95) कुमार्यां वयसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
