"""
6.3.82  वोपसर्जनस्य  —  VIDHI

Padaccheda: वा उपसर्जनस्य

वोपसर्जनस्य (6.3.82)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_82_vopasarjan_82"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.82"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vopasarjanasya",
    text_dev              = "वोपसर्जनस्य",
    padaccheda_dev        = "वा उपसर्जनस्य",
    why_dev               = "(सूत्रम् 6.3.82) वोपसर्जनस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
