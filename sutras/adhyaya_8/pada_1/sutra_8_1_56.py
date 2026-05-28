"""
8.1.56  यद्धितुपरं छन्दसि  —  VIDHI

Padaccheda: यत्-हि-तु-परम् छन्दसि

यद्धितुपरं छन्दसि (8.1.56)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_56_yadDitupar_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_56_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yadDituparaM Candasi",
    text_dev              = "यद्धितुपरं छन्दसि",
    padaccheda_dev        = "यत्-हि-तु-परम् छन्दसि",
    why_dev               = "(सूत्रम् 8.1.56) यद्धितुपरं छन्दसि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
