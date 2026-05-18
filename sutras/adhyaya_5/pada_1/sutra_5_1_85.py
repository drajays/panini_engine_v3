"""
5.1.85  समायाः खः  —  VIDHI

Padaccheda: समायाः खः

समायाः खः (5.1.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_85_samAyAH_85"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_85_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samAyAH KaH",
    text_dev              = "समायाः खः",
    padaccheda_dev        = "समायाः खः",
    why_dev               = "(सूत्रम् 5.1.85) समायाः खः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
