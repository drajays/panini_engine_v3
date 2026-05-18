"""
5.4.102  द्वित्रिभ्यामञ्जलेः  —  VIDHI

Padaccheda: द्वि-त्रिभ्याम् अञ्जलेः

द्वित्रिभ्यामञ्जलेः (5.4.102)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_102_dvitriByAm_102"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_102_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.102"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.102",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvitriByAmaYjaleH",
    text_dev              = "द्वित्रिभ्यामञ्जलेः",
    padaccheda_dev        = "द्वि-त्रिभ्याम् अञ्जलेः",
    why_dev               = "(सूत्रम् 5.4.102) द्वित्रिभ्यामञ्जलेः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
