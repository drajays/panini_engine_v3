"""
6.4.60  निष्ठायां अण्यदर्थे  —  VIDHI

Padaccheda: निष्ठायाम् अ-ण्यत्-अर्थे

निष्ठायां अण्यदर्थे (6.4.60)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_60_nizWAyAM_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_60_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizWAyAM aRyadarTe",
    text_dev              = "निष्ठायां अण्यदर्थे",
    padaccheda_dev        = "निष्ठायाम् अ-ण्यत्-अर्थे",
    why_dev               = "(सूत्रम् 6.4.60) निष्ठायां अण्यदर्थे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
