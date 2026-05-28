"""
5.4.9  जात्यन्ताच्छ बन्धुनि  —  VIDHI

Padaccheda: जाति-अन्तात् छ (लुप्तप्रथमान्तनिर्देशः) बन्धुनि

जात्यन्ताच्छ बन्धुनि (5.4.9)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_9_jAtyantAcC_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.9", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAtyantAcCa banDuni",
    text_dev              = "जात्यन्ताच्छ बन्धुनि",
    padaccheda_dev        = "जाति-अन्तात् छ (लुप्तप्रथमान्तनिर्देशः) बन्धुनि",
    why_dev               = "(सूत्रम् 5.4.9) जात्यन्ताच्छ बन्धुनि।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
