"""
5.3.14  इतराभ्योऽपि दृश्यन्ते  —  VIDHI

Padaccheda: इतराभ्यः अपि दृश्यन्ते (क्रियापदम्)

इतराभ्योऽपि दृश्यन्ते (5.3.14)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_14_itarAByop_14"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.14", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "itarAByo'pi dfSyante",
    text_dev              = "इतराभ्योऽपि दृश्यन्ते",
    padaccheda_dev        = "इतराभ्यः अपि दृश्यन्ते (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.3.14) इतराभ्योऽपि दृश्यन्ते।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
