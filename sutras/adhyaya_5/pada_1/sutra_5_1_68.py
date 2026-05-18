"""
5.1.68  पात्राद्घंश्च  —  VIDHI

Padaccheda: पात्रात् घन् च

पात्राद्घंश्च (5.1.68)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_68_pAtrAdGaMS_68"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_68_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pAtrAdGaMSca",
    text_dev              = "पात्राद्घंश्च",
    padaccheda_dev        = "पात्रात् घन् च",
    why_dev               = "(सूत्रम् 5.1.68) पात्राद्घंश्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
