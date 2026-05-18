"""
4.4.143  शिवशमरिष्टस्य करे  —  VIDHI

Padaccheda: शिव-शम्-अरिष्टस्य करे

शिवशमरिष्टस्य करे (4.4.143)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_143_SivaSamari_143"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_143_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.143"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.143",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SivaSamarizwasya kare",
    text_dev              = "शिवशमरिष्टस्य करे",
    padaccheda_dev        = "शिव-शम्-अरिष्टस्य करे",
    why_dev               = "(सूत्रम् 4.4.143) शिवशमरिष्टस्य करे।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
