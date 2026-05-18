"""
4.4.110  भवे छन्दसि  —  VIDHI

Padaccheda: भवे छन्दसि

भवे छन्दसि (4.4.110)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_110_Bave_110"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_110_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Bave Candasi",
    text_dev              = "भवे छन्दसि",
    padaccheda_dev        = "भवे छन्दसि",
    why_dev               = "(सूत्रम् 4.4.110) भवे छन्दसि।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
