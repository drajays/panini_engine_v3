"""
6.1.6  जक्षित्यादयः षट्  —  VIDHI

Padaccheda: जक्ष् (अविभक्तिकनिर्देशः) इति-आदयः षट्

जक्षित्यादयः षट् (6.1.6)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_6_jakzityAda_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_6_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jakzityAdayaH zaw",
    text_dev              = "जक्षित्यादयः षट्",
    padaccheda_dev        = "जक्ष् (अविभक्तिकनिर्देशः) इति-आदयः षट्",
    why_dev               = "(सूत्रम् 6.1.6) जक्षित्यादयः षट्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
