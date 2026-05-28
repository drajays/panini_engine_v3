"""
6.2.171  वा जाते  —  VIDHI

Padaccheda: वा जाते

वा जाते (6.2.171)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_171_vA_171"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.171"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.171",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA jAte",
    text_dev              = "वा जाते",
    padaccheda_dev        = "वा जाते",
    why_dev               = "(सूत्रम् 6.2.171) वा जाते।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
