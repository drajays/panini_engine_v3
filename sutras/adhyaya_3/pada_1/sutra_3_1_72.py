"""
3.1.72  संयसश्च  —  VIDHI

Padaccheda: संयसः च

Krt suffix rule from dhatu: संयसश्च (72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_72_saMyasaSca_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_72_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMyasaSca",
    text_dev              = "संयसश्च",
    padaccheda_dev        = "संयसः च",
    why_dev               = "धातोः [संयसश्च]-प्रत्ययः विहितः (३.१.72)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
