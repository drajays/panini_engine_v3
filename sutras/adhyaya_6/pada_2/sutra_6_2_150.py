"""
6.2.150  अनो भावकर्मवचनः  —  VIDHI

Padaccheda: अनः भावकर्मवचनः

अनो भावकर्मवचनः (6.2.150)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_150_ano_150"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_150_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.150"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.150",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ano BAvakarmavacanaH",
    text_dev              = "अनो भावकर्मवचनः",
    padaccheda_dev        = "अनः भावकर्मवचनः",
    why_dev               = "(सूत्रम् 6.2.150) अनो भावकर्मवचनः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
