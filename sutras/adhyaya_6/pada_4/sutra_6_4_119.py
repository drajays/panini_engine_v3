"""
6.4.119  घ्वसोरेद्धावभ्यासलोपश्च  —  VIDHI

Padaccheda: घु-असोः एत् हौ अभ्यास-लोपः च

घ्वसोरेद्धावभ्यासलोपश्च (6.4.119)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_119_GvasoredDA_119"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_119_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "GvasoredDAvaByAsalopaSca",
    text_dev              = "घ्वसोरेद्धावभ्यासलोपश्च",
    padaccheda_dev        = "घु-असोः एत् हौ अभ्यास-लोपः च",
    why_dev               = "(सूत्रम् 6.4.119) घ्वसोरेद्धावभ्यासलोपश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
