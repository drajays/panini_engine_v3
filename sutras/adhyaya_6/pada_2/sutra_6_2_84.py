"""
6.2.84  ग्रामेऽनिवसन्तः  —  VIDHI

Padaccheda: ग्रामे अनिवसन्तः

ग्रामेऽनिवसन्तः (6.2.84)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_84_grAmeniva_84"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_84_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.84"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grAme'nivasantaH",
    text_dev              = "ग्रामेऽनिवसन्तः",
    padaccheda_dev        = "ग्रामे अनिवसन्तः",
    why_dev               = "(सूत्रम् 6.2.84) ग्रामेऽनिवसन्तः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
