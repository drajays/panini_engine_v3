"""
6.3.95  सहस्य सध्रिः  —  VIDHI

Padaccheda: सहस्य सध्रिः

सहस्य सध्रिः (6.3.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_95_sahasya_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sahasya saDriH",
    text_dev              = "सहस्य सध्रिः",
    padaccheda_dev        = "सहस्य सध्रिः",
    why_dev               = "(सूत्रम् 6.3.95) सहस्य सध्रिः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
