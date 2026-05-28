"""
8.3.53  षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु  —  VIDHI

Padaccheda: षष्ठ्याः पति-पुत्र-पृष्ठ-पार-पद-पयस्-पोषेषु

षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु (8.3.53)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_53_zazWyAH_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zazWyAH patiputrapfzWapArapadapayaspozezu",
    text_dev              = "षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु",
    padaccheda_dev        = "षष्ठ्याः पति-पुत्र-पृष्ठ-पार-पद-पयस्-पोषेषु",
    why_dev               = "(सूत्रम् 8.3.53) षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
