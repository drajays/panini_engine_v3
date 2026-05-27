"""
2.2.37  वाऽऽहिताग्न्यादिषु  —  VIDHI

Padaccheda: वा आहित-अग्नि-आदिषु

In ahitagni etc. optionally (vibhasha).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_37_ahitagni_va"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("bahuvrIhi" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["bahuvrihi_kind"]             = "2.2.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA''hitAgnyAdizu",
    text_dev              = "वाऽऽहिताग्न्यादिषु",
    padaccheda_dev        = "वा आहित-अग्नि-आदिषु",
    why_dev               = "आहित-अग्नि-आदिषु वा (२.२.३७)।",
    anuvritti_from        = ('2.2.36',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
