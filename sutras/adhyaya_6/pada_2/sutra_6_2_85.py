"""
6.2.85  घोषादिषु  —  VIDHI

Padaccheda: घोष-आदिषु शालायाम्

घोषादिषु (6.2.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_85_GozAdizu_85"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "GozAdizu",
    text_dev              = "घोषादिषु",
    padaccheda_dev        = "घोष-आदिषु शालायाम्",
    why_dev               = "(सूत्रम् 6.2.85) घोषादिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
