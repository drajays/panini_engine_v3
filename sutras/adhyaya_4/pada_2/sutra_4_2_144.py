"""
4.2.144  विभाषाऽमनुष्ये  —  VIDHI

Padaccheda: विभाषा अमनुष्ये

विभाषाऽमनुष्ये (4.2.144)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_144_viBAzAman_144"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_144_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.144"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.144",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA'manuzye",
    text_dev              = "विभाषाऽमनुष्ये",
    padaccheda_dev        = "विभाषा अमनुष्ये",
    why_dev               = "(सूत्रम् 4.2.144) विभाषाऽमनुष्ये।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
