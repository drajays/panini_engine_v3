"""
4.3.90  अभिजनश्च  —  VIDHI

Padaccheda: अभिजनः च

अभिजनश्च (4.3.90)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_90_aBijanaSca_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_90_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aBijanaSca",
    text_dev              = "अभिजनश्च",
    padaccheda_dev        = "अभिजनः च",
    why_dev               = "(सूत्रम् 4.3.90) अभिजनश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
