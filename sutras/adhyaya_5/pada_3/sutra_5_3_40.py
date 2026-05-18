"""
5.3.40  अस्ताति च  —  VIDHI

Padaccheda: अस्ताति च

अस्ताति च (5.3.40)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_40_astAti_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_40_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "astAti ca",
    text_dev              = "अस्ताति च",
    padaccheda_dev        = "अस्ताति च",
    why_dev               = "(सूत्रम् 5.3.40) अस्ताति च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
