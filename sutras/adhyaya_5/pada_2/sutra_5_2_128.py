"""
5.2.128  द्वंद्वोपतापगर्ह्यात् प्राणिस्थादिनिः  —  VIDHI

Padaccheda: द्वन्द्व-उपताप-गर्ह्यात् प्राणि-स्थात् इनिः

द्वंद्वोपतापगर्ह्यात् प्राणिस्थादिनिः (5.2.128)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_128_dvaMdvopat_128"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_128_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.128"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.128",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvaMdvopatApagarhyAt prARisTAdiniH",
    text_dev              = "द्वंद्वोपतापगर्ह्यात् प्राणिस्थादिनिः",
    padaccheda_dev        = "द्वन्द्व-उपताप-गर्ह्यात् प्राणि-स्थात् इनिः",
    why_dev               = "(सूत्रम् 5.2.128) द्वंद्वोपतापगर्ह्यात् प्राणिस्थादिनिः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
