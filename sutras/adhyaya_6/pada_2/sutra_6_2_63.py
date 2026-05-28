"""
6.2.63  राजा च प्रशंसायाम्  —  VIDHI

Padaccheda: राजा च प्रशंसायाम्

राजा च प्रशंसायाम् (6.2.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_63_rAjA_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAjA ca praSaMsAyAm",
    text_dev              = "राजा च प्रशंसायाम्",
    padaccheda_dev        = "राजा च प्रशंसायाम्",
    why_dev               = "(सूत्रम् 6.2.63) राजा च प्रशंसायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
