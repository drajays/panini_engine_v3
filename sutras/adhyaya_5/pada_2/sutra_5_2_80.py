"""
5.2.80  उत्क उन्मनाः  —  VIDHI

Padaccheda: उत्कः उन्मनाः

उत्क उन्मनाः (5.2.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_80_utka_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_80_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "utka unmanAH",
    text_dev              = "उत्क उन्मनाः",
    padaccheda_dev        = "उत्कः उन्मनाः",
    why_dev               = "(सूत्रम् 5.2.80) उत्क उन्मनाः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
