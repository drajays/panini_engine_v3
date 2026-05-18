"""
7.3.13  दिशोऽमद्राणाम्  —  VIDHI

Padaccheda: दिशः अमद्राणाम्

दिशोऽमद्राणाम् (7.3.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_13_diSomadrA_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_13_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "diSo'madrARAm",
    text_dev              = "दिशोऽमद्राणाम्",
    padaccheda_dev        = "दिशः अमद्राणाम्",
    why_dev               = "(सूत्रम् 7.3.13) दिशोऽमद्राणाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
