"""
6.3.124  दस्ति  —  VIDHI

Padaccheda: दः ति

दस्ति (6.3.124)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_124_dasti_124"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_124_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dasti",
    text_dev              = "दस्ति",
    padaccheda_dev        = "दः ति",
    why_dev               = "(सूत्रम् 6.3.124) दस्ति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
