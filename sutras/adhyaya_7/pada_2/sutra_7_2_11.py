"""
7.2.11  श्र्युकः किति  —  VIDHI

Padaccheda: श्रि-उकः किति

श्र्युकः किति (7.2.11)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_11_SryukaH_11"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_11_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SryukaH kiti",
    text_dev              = "श्र्युकः किति",
    padaccheda_dev        = "श्रि-उकः किति",
    why_dev               = "(सूत्रम् 7.2.11) श्र्युकः किति।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
