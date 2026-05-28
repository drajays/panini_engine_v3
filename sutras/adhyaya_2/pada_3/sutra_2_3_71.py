"""
2.3.71  कृत्यानां कर्तरि वा  —  VIDHI

Padaccheda: कृत्यानाम् कर्तरि वा

krtya words optionally take kartri as agent.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_71_kartari_krtya_va"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kftyAnAM kartari vA",
    text_dev              = "कृत्यानां कर्तरि वा",
    padaccheda_dev        = "कृत्यानाम् कर्तरि वा",
    why_dev               = "कर्तरि कृत्यानाम् वा (२.३.७१)।",
    anuvritti_from        = ('2.3.65',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
