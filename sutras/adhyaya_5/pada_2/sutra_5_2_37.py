"""
5.2.37  प्रमाणे द्वयसज्दघ्नञ्मात्रचः  —  VIDHI

Padaccheda: प्रमाणे द्वयसच्-दघ्नच्-मात्रचः

प्रमाणे द्वयसज्दघ्नञ्मात्रचः (5.2.37)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_37_pramARe_37"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_37_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pramARe dvayasajdaGnaYmAtracaH",
    text_dev              = "प्रमाणे द्वयसज्दघ्नञ्मात्रचः",
    padaccheda_dev        = "प्रमाणे द्वयसच्-दघ्नच्-मात्रचः",
    why_dev               = "(सूत्रम् 5.2.37) प्रमाणे द्वयसज्दघ्नञ्मात्रचः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
