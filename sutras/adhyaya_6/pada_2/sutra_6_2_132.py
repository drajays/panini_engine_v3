"""
6.2.132  पुत्रः पुंभ्यः  —  VIDHI

Padaccheda: पुत्रः पुम्भ्यः

पुत्रः पुंभ्यः (6.2.132)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_132_putraH_132"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_132_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.132"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.132",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "putraH puMByaH",
    text_dev              = "पुत्रः पुंभ्यः",
    padaccheda_dev        = "पुत्रः पुम्भ्यः",
    why_dev               = "(सूत्रम् 6.2.132) पुत्रः पुंभ्यः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
