"""
5.4.62  निष्कुलान्निष्कोषणे  —  VIDHI

Padaccheda: निष्कुलात् निष्कोषणे

निष्कुलान्निष्कोषणे (5.4.62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_62_nizkulAnni_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_62_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizkulAnnizkozaRe",
    text_dev              = "निष्कुलान्निष्कोषणे",
    padaccheda_dev        = "निष्कुलात् निष्कोषणे",
    why_dev               = "(सूत्रम् 5.4.62) निष्कुलान्निष्कोषणे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
