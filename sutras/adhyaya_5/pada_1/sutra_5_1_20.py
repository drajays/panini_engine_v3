"""
5.1.20  असमासे निष्कादिभ्यः  —  VIDHI

Padaccheda: अ-समासे निष्क-आदिभ्यः

असमासे निष्कादिभ्यः (5.1.20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_20_asamAse_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_20_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asamAse nizkAdiByaH",
    text_dev              = "असमासे निष्कादिभ्यः",
    padaccheda_dev        = "अ-समासे निष्क-आदिभ्यः",
    why_dev               = "(सूत्रम् 5.1.20) असमासे निष्कादिभ्यः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
