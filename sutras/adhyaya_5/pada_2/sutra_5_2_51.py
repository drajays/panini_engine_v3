"""
5.2.51  षट्कतिकतिपयचतुरां थुक्  —  VIDHI

Padaccheda: षट्-कति-कतिपय-चतुराम् थुक्

षट्कतिकतिपयचतुरां थुक् (5.2.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_51_zawkatikat_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_51_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zawkatikatipayacaturAM Tuk",
    text_dev              = "षट्कतिकतिपयचतुरां थुक्",
    padaccheda_dev        = "षट्-कति-कतिपय-चतुराम् थुक्",
    why_dev               = "(सूत्रम् 5.2.51) षट्कतिकतिपयचतुरां थुक्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
