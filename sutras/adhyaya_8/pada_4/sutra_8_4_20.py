"""
8.4.20  अन्तः  —  VIDHI

Padaccheda: अन्तः

अन्तः (8.4.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_20_antaH_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_20_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "antaH",
    text_dev              = "अन्तः",
    padaccheda_dev        = "अन्तः",
    why_dev               = "(सूत्रम् 8.4.20) अन्तः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
