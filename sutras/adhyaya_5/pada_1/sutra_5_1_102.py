"""
5.1.102  योगाद्यच्च  —  VIDHI

Padaccheda: योगात् यत् च

योगाद्यच्च (5.1.102)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_102_yogAdyacca_102"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_102_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.102"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.102",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yogAdyacca",
    text_dev              = "योगाद्यच्च",
    padaccheda_dev        = "योगात् यत् च",
    why_dev               = "(सूत्रम् 5.1.102) योगाद्यच्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
