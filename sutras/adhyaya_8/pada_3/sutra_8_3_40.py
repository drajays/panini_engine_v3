"""
8.3.40  नमस्पुरसोर्गत्योः  —  VIDHI

Padaccheda: नमस् · पुरस् · गत्योः

नमस्पुरसोर्गत्योः (8.3.40)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_40_namaspuras_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_40_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "namaspurasorgatyoH",
    text_dev              = "नमस्पुरसोर्गत्योः",
    padaccheda_dev        = "नमस् · पुरस् · गत्योः",
    why_dev               = "(सूत्रम् 8.3.40) नमस्पुरसोर्गत्योः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
