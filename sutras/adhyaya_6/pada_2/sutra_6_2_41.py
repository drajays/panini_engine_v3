"""
6.2.41  गौः सादसादिसारथिषु  —  VIDHI

Padaccheda: गौः साद-सादि-सारथिषु

गौः सादसादिसारथिषु (6.2.41)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_41_gOH_41"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_41_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gOH sAdasAdisAraTizu",
    text_dev              = "गौः सादसादिसारथिषु",
    padaccheda_dev        = "गौः साद-सादि-सारथिषु",
    why_dev               = "(सूत्रम् 6.2.41) गौः सादसादिसारथिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
