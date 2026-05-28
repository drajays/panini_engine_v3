"""
6.2.70  अङ्गानि मैरेये  —  VIDHI

Padaccheda: अङ्गानि मैरेये

अङ्गानि मैरेये (6.2.70)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_70_aNgAni_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aNgAni mEreye",
    text_dev              = "अङ्गानि मैरेये",
    padaccheda_dev        = "अङ्गानि मैरेये",
    why_dev               = "(सूत्रम् 6.2.70) अङ्गानि मैरेये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
