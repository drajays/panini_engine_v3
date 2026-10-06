"""
5.3.76  अनुकम्पायाम्  —  VIDHI

Padaccheda: अनुकम्पायाम्

अनुकम्पायाम् (5.3.76)
Pāṭha: ashtadhyayi.com data.txt row i=53076 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_76_anukampAyA_76"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.76", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anukampAyAm",
    text_dev              = "अनुकम्पायाम्",
    samagra_slp1          = "anukampAyAm prAtipadikAt tiNaH ca kaH",
    samagra_dev           = "अनुकम्पायाम् प्रातिपदिकात् तिङः च कः",
    padaccheda_dev        = "अनुकम्पायाम्",
    why_dev               = "(सूत्रम् 5.3.76) अनुकम्पायाम्।",
    anuvritti_from        = ('5.3.70',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
