"""
5.1.32  विंशतिकात् खः  —  VIDHI

Padaccheda: विंशतिकात् खः

विंशतिकात् खः (5.1.32)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_32_viMSatikAt_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_32_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viMSatikAt KaH",
    text_dev              = "विंशतिकात् खः",
    padaccheda_dev        = "विंशतिकात् खः",
    why_dev               = "(सूत्रम् 5.1.32) विंशतिकात् खः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
