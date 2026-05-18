"""
5.2.67  उदराट्ठगाद्यूने  —  VIDHI

Padaccheda: उदरात् ठक् आद्यूने

उदराट्ठगाद्यूने (5.2.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_67_udarAwWagA_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_67_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udarAwWagAdyUne",
    text_dev              = "उदराट्ठगाद्यूने",
    padaccheda_dev        = "उदरात् ठक् आद्यूने",
    why_dev               = "(सूत्रम् 5.2.67) उदराट्ठगाद्यूने।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
