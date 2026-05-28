"""
5.2.93  इन्द्रियमिन्द्रलिंगमिन्द्रदृष्टमिन्द्रसृष्टमिन्द्रजुष्टम्इन्द्रदत्तमिति वा  —  VIDHI

Padaccheda: इन्द्रियम् इन्द्रलिङ्गम् इन्द्रदृष्टम् इन्द्रसृष्टम् इन्द्रजुष्टम् इन्द्रदत्तम् इति वा

इन्द्रियमिन्द्रलिंगमिन्द्रदृष्टमिन्द्रसृष्टमिन्द्रजुष्टम्इन्द्रदत्तमिति वा (5.2.93)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_93_indriyamin_93"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.93", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.93"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "indriyamindraliMgamindradfzwamindrasfzwamindrajuzwamindradattamiti vA",
    text_dev              = "इन्द्रियमिन्द्रलिंगमिन्द्रदृष्टमिन्द्रसृष्टमिन्द्रजुष्टम्इन्द्रदत्तमिति वा",
    padaccheda_dev        = "इन्द्रियम् इन्द्रलिङ्गम् इन्द्रदृष्टम् इन्द्रसृष्टम् इन्द्रजुष्टम् इन्द्रदत्तम् इति वा",
    why_dev               = "(सूत्रम् 5.2.93) इन्द्रियमिन्द्रलिंगमिन्द्रदृष्टमिन्द्रसृष्टमिन्द्रजुष्टम्इन्द्रदत्तमिति वा।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
