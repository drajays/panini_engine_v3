"""
5.3.86  ह्रस्वे  —  VIDHI

Padaccheda: ह्रस्वे

ह्रस्वे (5.3.86)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_86_hrasve_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_86_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hrasve",
    text_dev              = "ह्रस्वे",
    padaccheda_dev        = "ह्रस्वे",
    why_dev               = "(सूत्रम् 5.3.86) ह्रस्वे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
