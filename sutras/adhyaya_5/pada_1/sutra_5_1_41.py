"""
5.1.41  सर्वभूमिपृथिवीभ्यामणञौ  —  VIDHI

Padaccheda: सर्वभूमि-पृथिवीभ्याम् अण्-अञौ

सर्वभूमिपृथिवीभ्यामणञौ (5.1.41)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_41_sarvaBUmip_41"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_41_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sarvaBUmipfTivIByAmaRaYO",
    text_dev              = "सर्वभूमिपृथिवीभ्यामणञौ",
    padaccheda_dev        = "सर्वभूमि-पृथिवीभ्याम् अण्-अञौ",
    why_dev               = "(सूत्रम् 5.1.41) सर्वभूमिपृथिवीभ्यामणञौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
