"""
6.4.91  वा चित्तविरागे  —  VIDHI

Padaccheda: वा चित्तविरागे

वा चित्तविरागे (6.4.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_91_vA_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.91", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA cittavirAge",
    text_dev              = "वा चित्तविरागे",
    padaccheda_dev        = "वा चित्तविरागे",
    why_dev               = "(सूत्रम् 6.4.91) वा चित्तविरागे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
