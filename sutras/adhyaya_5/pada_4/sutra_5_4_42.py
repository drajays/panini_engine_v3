"""
5.4.42  बह्वल्पार्थाच्छस् कारकादन्यतरस्याम्  —  VIDHI

Padaccheda: बहु-अल्प-अर्थात् शस् कारकात् अन्यतरस्याम्

बह्वल्पार्थाच्छस् कारकादन्यतरस्याम् (5.4.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_42_bahvalpArT_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.42", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahvalpArTAcCas kArakAdanyatarasyAm",
    text_dev              = "बह्वल्पार्थाच्छस् कारकादन्यतरस्याम्",
    padaccheda_dev        = "बहु-अल्प-अर्थात् शस् कारकात् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 5.4.42) बह्वल्पार्थाच्छस् कारकादन्यतरस्याम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
