"""
6.4.52  निष्ठायां सेटि  —  VIDHI

Padaccheda: निष्ठायाम् सेटि

निष्ठायां सेटि (6.4.52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_52_nizWAyAM_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_52_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizWAyAM sewi",
    text_dev              = "निष्ठायां सेटि",
    padaccheda_dev        = "निष्ठायाम् सेटि",
    why_dev               = "(सूत्रम् 6.4.52) निष्ठायां सेटि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
