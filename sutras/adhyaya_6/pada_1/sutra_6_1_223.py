"""
6.1.223  समासस्य  —  VIDHI

Padaccheda: समासस्य

समासस्य (6.1.223)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_223_samAsasya_223"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_223_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.223"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.223",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samAsasya",
    text_dev              = "समासस्य",
    padaccheda_dev        = "समासस्य",
    why_dev               = "(सूत्रम् 6.1.223) समासस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
