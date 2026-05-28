"""
6.4.133  श्वयुवमघोनामतद्धिते  —  VIDHI

Padaccheda: श्व-युव-मघोनाम् अ-तद्धिते

श्वयुवमघोनामतद्धिते (6.4.133)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_133_SvayuvamaG_133"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.133", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.133"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.133",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SvayuvamaGonAmatadDite",
    text_dev              = "श्वयुवमघोनामतद्धिते",
    padaccheda_dev        = "श्व-युव-मघोनाम् अ-तद्धिते",
    why_dev               = "(सूत्रम् 6.4.133) श्वयुवमघोनामतद्धिते।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
