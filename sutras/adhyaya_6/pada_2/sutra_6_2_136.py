"""
6.2.136  कुण्डं वनम्  —  VIDHI

Padaccheda: कुण्डम् वनम्

कुण्डं वनम् (6.2.136)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_136_kuRqaM_136"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_136_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.136"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.136",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kuRqaM vanam",
    text_dev              = "कुण्डं वनम्",
    padaccheda_dev        = "कुण्डम् वनम्",
    why_dev               = "(सूत्रम् 6.2.136) कुण्डं वनम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
