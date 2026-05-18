"""
7.4.44  विभाषा छन्दसि  —  VIDHI

Padaccheda: विभाषा छन्दसि

विभाषा छन्दसि (7.4.44)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_44_viBAzA_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_44_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA Candasi",
    text_dev              = "विभाषा छन्दसि",
    padaccheda_dev        = "विभाषा छन्दसि",
    why_dev               = "(सूत्रम् 7.4.44) विभाषा छन्दसि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
