"""
4.3.130  न दण्डमाणवान्तेवासिषु  —  VIDHI

Padaccheda: न दण्डमाणव-अन्तेवासिषु

न दण्डमाणवान्तेवासिषु (4.3.130)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_130_na_130"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_130_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.130"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na daRqamARavAntevAsizu",
    text_dev              = "न दण्डमाणवान्तेवासिषु",
    padaccheda_dev        = "न दण्डमाणव-अन्तेवासिषु",
    why_dev               = "(सूत्रम् 4.3.130) न दण्डमाणवान्तेवासिषु।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
