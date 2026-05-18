"""
4.1.17  प्राचां ष्फ तद्धितः  —  VIDHI

Padaccheda: प्राचाम् ष्फः तद्धितः

प्राचां ष्फ तद्धितः (4.1.17)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_17_prAcAM_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_17_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAcAM zPa tadDitaH",
    text_dev              = "प्राचां ष्फ तद्धितः",
    padaccheda_dev        = "प्राचाम् ष्फः तद्धितः",
    why_dev               = "(सूत्रम् 4.1.17) प्राचां ष्फ तद्धितः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
