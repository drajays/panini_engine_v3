"""
6.2.123  तत्पुरुषे शालायां नपुंसके  —  VIDHI

Padaccheda: तत्पुरुषे शालायाम् नपुंसके

तत्पुरुषे शालायां नपुंसके (6.2.123)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_123_tatpuruze_123"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_123_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.123"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatpuruze SAlAyAM napuMsake",
    text_dev              = "तत्पुरुषे शालायां नपुंसके",
    padaccheda_dev        = "तत्पुरुषे शालायाम् नपुंसके",
    why_dev               = "(सूत्रम् 6.2.123) तत्पुरुषे शालायां नपुंसके।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
