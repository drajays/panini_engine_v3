"""
4.2.133  कच्छादिभ्यश्च  —  VIDHI

Padaccheda: कच्छ-आदिभ्यः च

कच्छादिभ्यश्च (4.2.133)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_133_kacCAdiBya_133"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.133", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.133"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.133",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kacCAdiByaSca",
    text_dev              = "कच्छादिभ्यश्च",
    padaccheda_dev        = "कच्छ-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.2.133) कच्छादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
