"""
5.2.65  धनहिरण्यात् कामे  —  VIDHI

Padaccheda: धन-हिरण्यात् कामे

धनहिरण्यात् कामे (5.2.65)
Pāṭha: ashtadhyayi.com data.txt row i=52065 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_65_DanahiraRy_65"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.65", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DanahiraRyAt kAme",
    text_dev              = "धनहिरण्यात् कामे",
    samagra_slp1          = "tatra kAme iti Dana-hiraRyAt kan",
    samagra_dev           = "'तत्र कामे' (इति) धन-हिरण्यात् कन्",
    padaccheda_dev        = "धन-हिरण्यात् कामे",
    why_dev               = "(सूत्रम् 5.2.65) धनहिरण्यात् कामे।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
