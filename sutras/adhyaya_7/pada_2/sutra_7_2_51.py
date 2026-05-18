"""
7.2.51  पूङश्च  —  VIDHI

Padaccheda: पूङः च

पूङश्च (7.2.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_51_pUNaSca_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_51_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUNaSca",
    text_dev              = "पूङश्च",
    padaccheda_dev        = "पूङः च",
    why_dev               = "(सूत्रम् 7.2.51) पूङश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
