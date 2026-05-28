"""
3.4.75  ताभ्यामन्यत्रोणादयः  —  VIDHI

Padaccheda: ताभ्याम् अन्यत्र उण्-आदयः

krt-suffix rule: ताभ्यामन्यत्रोणादयः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_75_tAByAmanya_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("3_4_75_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tAByAmanyatroRAdayaH",
    text_dev              = "ताभ्यामन्यत्रोणादयः",
    padaccheda_dev        = "ताभ्याम् अन्यत्र उण्-आदयः",
    why_dev               = "धातोः प्रत्ययः (३.4.75)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
