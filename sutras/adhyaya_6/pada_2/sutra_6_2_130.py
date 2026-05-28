"""
6.2.130  अकर्मधारये राज्यम्  —  VIDHI

Padaccheda: अ-कर्मधारये राज्यम्

अकर्मधारये राज्यम् (6.2.130)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_130_akarmaDAra_130"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.130"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "akarmaDAraye rAjyam",
    text_dev              = "अकर्मधारये राज्यम्",
    padaccheda_dev        = "अ-कर्मधारये राज्यम्",
    why_dev               = "(सूत्रम् 6.2.130) अकर्मधारये राज्यम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
