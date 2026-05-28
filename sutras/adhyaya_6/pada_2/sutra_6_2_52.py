"""
6.2.52  अनिगन्तोऽञ्चतौ वप्रत्यये  —  VIDHI

Padaccheda: अन्-इक्-अन्तः अञ्चतौ व-प्रत्यये

अनिगन्तोऽञ्चतौ वप्रत्यये (6.2.52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_52_anigantoY_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aniganto'YcatO vapratyaye",
    text_dev              = "अनिगन्तोऽञ्चतौ वप्रत्यये",
    padaccheda_dev        = "अन्-इक्-अन्तः अञ्चतौ व-प्रत्यये",
    why_dev               = "(सूत्रम् 6.2.52) अनिगन्तोऽञ्चतौ वप्रत्यये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
