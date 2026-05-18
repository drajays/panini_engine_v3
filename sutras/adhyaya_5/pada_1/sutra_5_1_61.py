"""
5.1.61  सप्तनोऽञ् छन्दसि  —  VIDHI

Padaccheda: सप्तनः अञ् छन्दसि

सप्तनोऽञ् छन्दसि (5.1.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_61_saptanoY_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saptano'Y Candasi",
    text_dev              = "सप्तनोऽञ् छन्दसि",
    padaccheda_dev        = "सप्तनः अञ् छन्दसि",
    why_dev               = "(सूत्रम् 5.1.61) सप्तनोऽञ् छन्दसि।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
