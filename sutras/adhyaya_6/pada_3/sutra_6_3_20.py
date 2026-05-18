"""
6.3.20  स्थे च भाषायाम्  —  VIDHI

Padaccheda: स्थे च भाषायाम्

स्थे च भाषायाम् (6.3.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_20_sTe_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_20_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTe ca BAzAyAm",
    text_dev              = "स्थे च भाषायाम्",
    padaccheda_dev        = "स्थे च भाषायाम्",
    why_dev               = "(सूत्रम् 6.3.20) स्थे च भाषायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
