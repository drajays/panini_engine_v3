"""
5.1.49  भागाद्यच्च  —  VIDHI

Padaccheda: भागात् यत् च

भागाद्यच्च (5.1.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_49_BAgAdyacca_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_49_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BAgAdyacca",
    text_dev              = "भागाद्यच्च",
    padaccheda_dev        = "भागात् यत् च",
    why_dev               = "(सूत्रम् 5.1.49) भागाद्यच्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
