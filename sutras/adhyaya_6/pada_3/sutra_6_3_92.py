"""
6.3.92  विष्वग्देवयोश्च टेरद्र्यञ्चतौ वप्रत्यये  —  VIDHI

Padaccheda: विष्वक्-देवयोः च टेः अद्रि (लुप्तप्रथमान्तनिर्देशः) अञ्चतौ व-प्रत्यये

विष्वग्देवयोश्च टेरद्र्यञ्चतौ वप्रत्यये (6.3.92)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_92_vizvagdeva_92"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_92_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.92"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vizvagdevayoSca weradryaYcatO vapratyaye",
    text_dev              = "विष्वग्देवयोश्च टेरद्र्यञ्चतौ वप्रत्यये",
    padaccheda_dev        = "विष्वक्-देवयोः च टेः अद्रि (लुप्तप्रथमान्तनिर्देशः) अञ्चतौ व-प्रत्यये",
    why_dev               = "(सूत्रम् 6.3.92) विष्वग्देवयोश्च टेरद्र्यञ्चतौ वप्रत्यये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
