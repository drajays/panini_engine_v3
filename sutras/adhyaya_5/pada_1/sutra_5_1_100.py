"""
5.1.100  कर्मवेषाद्यत्  —  VIDHI

Padaccheda: कर्म-वेषात् यत्

कर्मवेषाद्यत् (5.1.100)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_100_karmavezAd_100"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_100_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmavezAdyat",
    text_dev              = "कर्मवेषाद्यत्",
    padaccheda_dev        = "कर्म-वेषात् यत्",
    why_dev               = "(सूत्रम् 5.1.100) कर्मवेषाद्यत्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
