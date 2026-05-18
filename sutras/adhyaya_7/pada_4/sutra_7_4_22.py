"""
7.4.22  अयङ् यि क्ङिति  —  VIDHI

Padaccheda: अयङ् यि क्ङिति

अयङ् यि क्ङिति (7.4.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_22_ayaN_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_22_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ayaN yi kNiti",
    text_dev              = "अयङ् यि क्ङिति",
    padaccheda_dev        = "अयङ् यि क्ङिति",
    why_dev               = "(सूत्रम् 7.4.22) अयङ् यि क्ङिति।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
