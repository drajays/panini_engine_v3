"""
5.1.122  पृथ्वादिभ्य इमनिज्वा  —  VIDHI

Padaccheda: पृथु-आदिभ्यः इमनिच् वा

पृथ्वादिभ्य इमनिज्वा (5.1.122)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_122_pfTvAdiBya_122"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.122", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pfTvAdiBya imanijvA",
    text_dev              = "पृथ्वादिभ्य इमनिज्वा",
    padaccheda_dev        = "पृथु-आदिभ्यः इमनिच् वा",
    why_dev               = "(सूत्रम् 5.1.122) पृथ्वादिभ्य इमनिज्वा।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
