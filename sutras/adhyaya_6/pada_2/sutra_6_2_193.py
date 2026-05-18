"""
6.2.193  प्रतेरंश्वादयस्तत्पुरुषे  —  VIDHI

Padaccheda: प्रतेः अंशु-आदयः तत्पुरुषे

प्रतेरंश्वादयस्तत्पुरुषे (6.2.193)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_193_prateraMSv_193"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_193_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.193"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.193",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prateraMSvAdayastatpuruze",
    text_dev              = "प्रतेरंश्वादयस्तत्पुरुषे",
    padaccheda_dev        = "प्रतेः अंशु-आदयः तत्पुरुषे",
    why_dev               = "(सूत्रम् 6.2.193) प्रतेरंश्वादयस्तत्पुरुषे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
