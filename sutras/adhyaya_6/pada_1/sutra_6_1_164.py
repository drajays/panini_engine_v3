"""
6.1.164  तद्धितस्य  —  VIDHI

Padaccheda: तद्धितस्य

तद्धितस्य (6.1.164)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_164_tadDitasya_164"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.164"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.164",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadDitasya",
    text_dev              = "तद्धितस्य",
    padaccheda_dev        = "तद्धितस्य",
    why_dev               = "(सूत्रम् 6.1.164) तद्धितस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
