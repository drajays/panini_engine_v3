"""
6.4.28  स्यदो जवे  —  VIDHI

Padaccheda: स्यदः जवे

स्यदो जवे (6.4.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_28_syado_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_28_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "syado jave",
    text_dev              = "स्यदो जवे",
    padaccheda_dev        = "स्यदः जवे",
    why_dev               = "(सूत्रम् 6.4.28) स्यदो जवे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
