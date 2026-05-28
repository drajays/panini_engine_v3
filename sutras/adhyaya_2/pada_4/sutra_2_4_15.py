"""
2.4.15  अधिकरणैतावत्त्वे च  —  VIDHI

Padaccheda: अधिकरण-एतावत्त्वे च

Also in adhikarana-etavattva context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_15_adhikarana_etavat"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("dvandva_samasa" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.4.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDikaraREtAvattve ca",
    text_dev              = "अधिकरणैतावत्त्वे च",
    padaccheda_dev        = "अधिकरण-एतावत्त्वे च",
    why_dev               = "अधिकरण-एतावत्त्वे च (२.४.१५)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
