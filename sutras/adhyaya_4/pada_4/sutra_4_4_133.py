"""
4.4.133  पूर्वैः कृतमिनियौ च  —  VIDHI

Padaccheda: पूर्वैः कृतम् इनि-यौ च

पूर्वैः कृतमिनियौ च (4.4.133)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_133_pUrvEH_133"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.133", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.133"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.133",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvEH kftaminiyO ca",
    text_dev              = "पूर्वैः कृतमिनियौ च",
    padaccheda_dev        = "पूर्वैः कृतम् इनि-यौ च",
    why_dev               = "(सूत्रम् 4.4.133) पूर्वैः कृतमिनियौ च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
