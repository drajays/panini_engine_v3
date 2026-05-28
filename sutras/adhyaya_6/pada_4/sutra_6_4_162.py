"""
6.4.162  विभाषर्जोश्छन्दसि  —  VIDHI

Padaccheda: विभाषा ऋजोः छन्दसि

विभाषर्जोश्छन्दसि (6.4.162)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_162_viBAzarjoS_162"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.162", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.162"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.162",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzarjoSCandasi",
    text_dev              = "विभाषर्जोश्छन्दसि",
    padaccheda_dev        = "विभाषा ऋजोः छन्दसि",
    why_dev               = "(सूत्रम् 6.4.162) विभाषर्जोश्छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
