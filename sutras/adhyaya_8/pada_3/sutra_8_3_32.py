"""
8.3.32  ङमो ह्रस्वादचि ङमुण्नित्यम्  —  VIDHI

Padaccheda: ङमः ह्रस्वात् अचि ङमुट् नित्यम्

ङमो ह्रस्वादचि ङमुण्नित्यम् (8.3.32)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_32_Namo_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_32_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Namo hrasvAdaci NamuRnityam",
    text_dev              = "ङमो ह्रस्वादचि ङमुण्नित्यम्",
    padaccheda_dev        = "ङमः ह्रस्वात् अचि ङमुट् नित्यम्",
    why_dev               = "(सूत्रम् 8.3.32) ङमो ह्रस्वादचि ङमुण्नित्यम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
