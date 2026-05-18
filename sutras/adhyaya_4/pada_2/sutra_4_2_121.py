"""
4.2.121  धन्वयोपधाद्वुञ्  —  VIDHI

Padaccheda: धन्व-य-उपधात् वुञ्

धन्वयोपधाद्वुञ् (4.2.121)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_121_DanvayopaD_121"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_121_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DanvayopaDAdvuY",
    text_dev              = "धन्वयोपधाद्वुञ्",
    padaccheda_dev        = "धन्व-य-उपधात् वुञ्",
    why_dev               = "(सूत्रम् 4.2.121) धन्वयोपधाद्वुञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
