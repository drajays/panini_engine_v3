"""
6.4.63  दीङो युडचि क्ङिति  —  VIDHI

Padaccheda: दीङः युट् अचि क्ङिति

दीङो युडचि क्ङिति (6.4.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_63_dINo_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_63_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dINo yuqaci kNiti",
    text_dev              = "दीङो युडचि क्ङिति",
    padaccheda_dev        = "दीङः युट् अचि क्ङिति",
    why_dev               = "(सूत्रम् 6.4.63) दीङो युडचि क्ङिति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
