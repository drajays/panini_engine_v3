"""
6.3.27  ईदग्नेः सोमवरुणयोः  —  VIDHI

Padaccheda: ईत् अग्नेः सोमवरुणयोः

ईदग्नेः सोमवरुणयोः (6.3.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_27_IdagneH_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "IdagneH somavaruRayoH",
    text_dev              = "ईदग्नेः सोमवरुणयोः",
    padaccheda_dev        = "ईत् अग्नेः सोमवरुणयोः",
    why_dev               = "(सूत्रम् 6.3.27) ईदग्नेः सोमवरुणयोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
