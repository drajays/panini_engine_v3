"""
5.2.34  उपाधिभ्यां त्यकन्नासन्नारूढयोः  —  VIDHI

Padaccheda: उप-अधिभ्याम् त्यकन् आसन्न-आरूढयोः

उपाधिभ्यां त्यकन्नासन्नारूढयोः (5.2.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_34_upADiByAM_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.34", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upADiByAM tyakannAsannArUQayoH",
    text_dev              = "उपाधिभ्यां त्यकन्नासन्नारूढयोः",
    padaccheda_dev        = "उप-अधिभ्याम् त्यकन् आसन्न-आरूढयोः",
    why_dev               = "(सूत्रम् 5.2.34) उपाधिभ्यां त्यकन्नासन्नारूढयोः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
