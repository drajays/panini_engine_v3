"""
5.3.117  पर्श्वादियौधेयादिभ्यामणञौ  —  VIDHI

Padaccheda: पर्शु-आदि-यौधेय-आदिभ्याम् अण्-अञौ

पर्श्वादियौधेयादिभ्यामणञौ (5.3.117)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_117_parSvAdiyO_117"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_117_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parSvAdiyODeyAdiByAmaRaYO",
    text_dev              = "पर्श्वादियौधेयादिभ्यामणञौ",
    padaccheda_dev        = "पर्शु-आदि-यौधेय-आदिभ्याम् अण्-अञौ",
    why_dev               = "(सूत्रम् 5.3.117) पर्श्वादियौधेयादिभ्यामणञौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
