"""
6.4.102  श्रुशृणुपॄकृवृभ्यश्छन्दसि  —  VIDHI

Padaccheda: श्रु-शृणु-पॄ-कृ-वृभ्यः छन्दसि

श्रुशृणुपॄकृवृभ्यश्छन्दसि (6.4.102)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_102_SruSfRupFk_102"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_102_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.102"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.102",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SruSfRupFkfvfByaSCandasi",
    text_dev              = "श्रुशृणुपॄकृवृभ्यश्छन्दसि",
    padaccheda_dev        = "श्रु-शृणु-पॄ-कृ-वृभ्यः छन्दसि",
    why_dev               = "(सूत्रम् 6.4.102) श्रुशृणुपॄकृवृभ्यश्छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
