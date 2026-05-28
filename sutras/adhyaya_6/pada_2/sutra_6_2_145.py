"""
6.2.145  सूपमानात् क्तः  —  VIDHI

Padaccheda: सु-उपमानात् क्तः

सूपमानात् क्तः (6.2.145)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_145_sUpamAnAt_145"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.145"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.145",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sUpamAnAt ktaH",
    text_dev              = "सूपमानात् क्तः",
    padaccheda_dev        = "सु-उपमानात् क्तः",
    why_dev               = "(सूत्रम् 6.2.145) सूपमानात् क्तः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
