"""
4.2.60  क्रतूक्थादिसूत्रान्ताट्ठक्  —  VIDHI

Padaccheda: क्रतु-उक्थ-आदि-सूत्र-अन्तात् ठक्

क्रतूक्थादिसूत्रान्ताट्ठक् (4.2.60)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_60_kratUkTAdi_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.60", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kratUkTAdisUtrAntAwWak",
    text_dev              = "क्रतूक्थादिसूत्रान्ताट्ठक्",
    padaccheda_dev        = "क्रतु-उक्थ-आदि-सूत्र-अन्तात् ठक्",
    why_dev               = "(सूत्रम् 4.2.60) क्रतूक्थादिसूत्रान्ताट्ठक्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
