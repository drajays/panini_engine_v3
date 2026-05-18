"""
4.1.46  नित्यं छन्दसि  —  VIDHI

Padaccheda: नित्यम् छन्दसि

नित्यं छन्दसि (4.1.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_46_nityaM_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_46_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityaM Candasi",
    text_dev              = "नित्यं छन्दसि",
    padaccheda_dev        = "नित्यम् छन्दसि",
    why_dev               = "(सूत्रम् 4.1.46) नित्यं छन्दसि।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
