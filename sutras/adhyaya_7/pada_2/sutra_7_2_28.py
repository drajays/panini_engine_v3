"""
7.2.28  रुष्यमत्वरसंघुषास्वनाम्  —  VIDHI

Padaccheda: रुषि-अम-त्वर-संघुष-आस्वनाम्

रुष्यमत्वरसंघुषास्वनाम् (7.2.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_28_ruzyamatva_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_28_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ruzyamatvarasaMGuzAsvanAm",
    text_dev              = "रुष्यमत्वरसंघुषास्वनाम्",
    padaccheda_dev        = "रुषि-अम-त्वर-संघुष-आस्वनाम्",
    why_dev               = "(सूत्रम् 7.2.28) रुष्यमत्वरसंघुषास्वनाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
