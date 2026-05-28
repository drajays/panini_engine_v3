"""
4.2.56  संग्रामे प्रयोजनयोद्धृभ्यः  —  VIDHI

Padaccheda: सङ्‍ग्रामे प्रयोजन-योद्धृभ्यः

संग्रामे प्रयोजनयोद्धृभ्यः (4.2.56)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_56_saMgrAme_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.56", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMgrAme prayojanayodDfByaH",
    text_dev              = "संग्रामे प्रयोजनयोद्धृभ्यः",
    padaccheda_dev        = "सङ्‍ग्रामे प्रयोजन-योद्धृभ्यः",
    why_dev               = "(सूत्रम् 4.2.56) संग्रामे प्रयोजनयोद्धृभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
