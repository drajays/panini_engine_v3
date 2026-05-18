"""
8.3.112  सिचो यङि  —  VIDHI

Padaccheda: सिचः यङि

सिचो यङि (8.3.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_112_sico_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_112_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sico yaNi",
    text_dev              = "सिचो यङि",
    padaccheda_dev        = "सिचः यङि",
    why_dev               = "(सूत्रम् 8.3.112) सिचो यङि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
