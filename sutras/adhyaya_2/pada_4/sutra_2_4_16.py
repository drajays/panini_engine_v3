"""
2.4.16  विभाषा समीपे  —  VIDHI

Padaccheda: विभाषा समीपे

Optional dvandva in proximity context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_16_samipe_vibhasa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_16_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.4.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA samIpe",
    text_dev              = "विभाषा समीपे",
    padaccheda_dev        = "विभाषा समीपे",
    why_dev               = "समीपे विभाषा (२.४.१६)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
