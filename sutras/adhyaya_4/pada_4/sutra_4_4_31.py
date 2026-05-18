"""
4.4.31  कुसीददशैकादशात् ष्ठन्ष्ठचौ  —  VIDHI

Padaccheda: कुसीद-दशैकादशात् ष्ठन्-ष्ठचौ

कुसीददशैकादशात् ष्ठन्ष्ठचौ (4.4.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_31_kusIdadaSE_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kusIdadaSEkAdaSAt zWanzWacO",
    text_dev              = "कुसीददशैकादशात् ष्ठन्ष्ठचौ",
    padaccheda_dev        = "कुसीद-दशैकादशात् ष्ठन्-ष्ठचौ",
    why_dev               = "(सूत्रम् 4.4.31) कुसीददशैकादशात् ष्ठन्ष्ठचौ।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
