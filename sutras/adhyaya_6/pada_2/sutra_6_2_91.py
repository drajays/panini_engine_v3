"""
6.2.91  न भूताधिकसंजीवमद्राश्मकज्जलम्  —  VIDHI

Padaccheda: न भूत-अधिक-संजीव-मद्र-अश्म-कज्जलम्

न भूताधिकसंजीवमद्राश्मकज्जलम् (6.2.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_91_na_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na BUtADikasaMjIvamadrASmakajjalam",
    text_dev              = "न भूताधिकसंजीवमद्राश्मकज्जलम्",
    padaccheda_dev        = "न भूत-अधिक-संजीव-मद्र-अश्म-कज्जलम्",
    why_dev               = "(सूत्रम् 6.2.91) न भूताधिकसंजीवमद्राश्मकज्जलम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
