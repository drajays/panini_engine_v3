"""
6.2.153  ऊनार्थकलहं तृतीयायाः  —  VIDHI

Padaccheda: ऊन-अर्थ-कलहम् तृतीयायाः

ऊनार्थकलहं तृतीयायाः (6.2.153)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_153_UnArTakala_153"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.153"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.153",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UnArTakalahaM tftIyAyAH",
    text_dev              = "ऊनार्थकलहं तृतीयायाः",
    padaccheda_dev        = "ऊन-अर्थ-कलहम् तृतीयायाः",
    why_dev               = "(सूत्रम् 6.2.153) ऊनार्थकलहं तृतीयायाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
