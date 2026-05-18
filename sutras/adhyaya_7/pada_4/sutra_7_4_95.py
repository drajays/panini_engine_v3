"""
7.4.95  अत् स्मृदृत्वरप्रथम्रदस्तॄस्पशाम्  —  VIDHI

Padaccheda: अत् स्मृ-दृ-त्वर-प्रथ-म्रद-स्तॄ-स्पशाम्

अत् स्मृदृत्वरप्रथम्रदस्तॄस्पशाम् (7.4.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_95_at_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_95_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "at smfdftvarapraTamradastFspaSAm",
    text_dev              = "अत् स्मृदृत्वरप्रथम्रदस्तॄस्पशाम्",
    padaccheda_dev        = "अत् स्मृ-दृ-त्वर-प्रथ-म्रद-स्तॄ-स्पशाम्",
    why_dev               = "(सूत्रम् 7.4.95) अत् स्मृदृत्वरप्रथम्रदस्तॄस्पशाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
