"""
6.3.62  एक तद्धिते च  —  VIDHI

Padaccheda: एक (लुप्तषष्ठ्यन्तनिर्देशः) तद्धिते च

एक तद्धिते च (6.3.62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_62_eka_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_62_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "eka tadDite ca",
    text_dev              = "एक तद्धिते च",
    padaccheda_dev        = "एक (लुप्तषष्ठ्यन्तनिर्देशः) तद्धिते च",
    why_dev               = "(सूत्रम् 6.3.62) एक तद्धिते च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
