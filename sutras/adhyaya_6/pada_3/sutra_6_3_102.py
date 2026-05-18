"""
6.3.102  रथवदयोश्च  —  VIDHI

Padaccheda: रथ-वदयोः च

रथवदयोश्च (6.3.102)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_102_raTavadayo_102"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_102_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.102"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.102",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "raTavadayoSca",
    text_dev              = "रथवदयोश्च",
    padaccheda_dev        = "रथ-वदयोः च",
    why_dev               = "(सूत्रम् 6.3.102) रथवदयोश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
