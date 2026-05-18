"""
5.4.96  अतेः शुनः  —  VIDHI

Padaccheda: अतेः शुनः

अतेः शुनः (5.4.96)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_96_ateH_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_96_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ateH SunaH",
    text_dev              = "अतेः शुनः",
    padaccheda_dev        = "अतेः शुनः",
    why_dev               = "(सूत्रम् 5.4.96) अतेः शुनः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
