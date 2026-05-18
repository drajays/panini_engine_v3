"""
4.1.130  आरगुदीचाम्  —  VIDHI

Padaccheda: आरक् उदीचाम्

आरगुदीचाम् (4.1.130)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_130_AragudIcAm_130"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_130_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.130"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AragudIcAm",
    text_dev              = "आरगुदीचाम्",
    padaccheda_dev        = "आरक् उदीचाम्",
    why_dev               = "(सूत्रम् 4.1.130) आरगुदीचाम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
