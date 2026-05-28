"""
6.1.179  षट्त्रिचतुर्भ्यो हलादिः  —  VIDHI

Padaccheda: षट्-त्रि-चतुर्भ्यः हल्-आदिः

षट्त्रिचतुर्भ्यो हलादिः (6.1.179)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_179_zawtricatu_179"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.179"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.179",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zawtricaturByo halAdiH",
    text_dev              = "षट्त्रिचतुर्भ्यो हलादिः",
    padaccheda_dev        = "षट्-त्रि-चतुर्भ्यः हल्-आदिः",
    why_dev               = "(सूत्रम् 6.1.179) षट्त्रिचतुर्भ्यो हलादिः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
