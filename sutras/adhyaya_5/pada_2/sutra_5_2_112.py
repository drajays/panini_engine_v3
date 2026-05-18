"""
5.2.112  रजःकृष्यासुतिपरिषदो वलच्  —  VIDHI

Padaccheda: रजः-कृषि-असुति-परिषदः वलच्

रजःकृष्यासुतिपरिषदो वलच् (5.2.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_112_rajaHkfzyA_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_112_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rajaHkfzyAsutiparizado valac",
    text_dev              = "रजःकृष्यासुतिपरिषदो वलच्",
    padaccheda_dev        = "रजः-कृषि-असुति-परिषदः वलच्",
    why_dev               = "(सूत्रम् 5.2.112) रजःकृष्यासुतिपरिषदो वलच्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
