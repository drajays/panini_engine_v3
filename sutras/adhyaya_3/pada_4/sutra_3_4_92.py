"""
3.4.92  आडुत्तमस्य पिच्च  —  VIDHI

Padaccheda: आट् उत्तमस्य पित् च

krt-suffix rule: आडुत्तमस्य पिच्च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_92_Aquttamasy_92"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_92_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.92"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Aquttamasya picca",
    text_dev              = "आडुत्तमस्य पिच्च",
    padaccheda_dev        = "आट् उत्तमस्य पित् च",
    why_dev               = "धातोः प्रत्ययः (३.4.92)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
