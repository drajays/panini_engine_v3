"""
6.2.127  चीरमुपमानम्  —  VIDHI

Padaccheda: चीरम् उपमानम्

चीरमुपमानम् (6.2.127)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_127_cIramupamA_127"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_127_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cIramupamAnam",
    text_dev              = "चीरमुपमानम्",
    padaccheda_dev        = "चीरम् उपमानम्",
    why_dev               = "(सूत्रम् 6.2.127) चीरमुपमानम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
