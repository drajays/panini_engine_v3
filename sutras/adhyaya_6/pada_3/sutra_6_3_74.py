"""
6.3.74  तस्मान्नुडचि  —  VIDHI

Padaccheda: तस्मात् नुट् अचि

तस्मान्नुडचि (6.3.74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_74_tasmAnnuqa_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasmAnnuqaci",
    text_dev              = "तस्मान्नुडचि",
    padaccheda_dev        = "तस्मात् नुट् अचि",
    why_dev               = "(सूत्रम् 6.3.74) तस्मान्नुडचि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
