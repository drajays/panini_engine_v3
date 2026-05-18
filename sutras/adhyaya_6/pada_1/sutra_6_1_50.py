"""
6.1.50  मीनातिमिनोतिदीङां ल्यपि च  —  VIDHI

Padaccheda: मीनाति-मिनोति-दीङाम् ल्यपि च

मीनातिमिनोतिदीङां ल्यपि च (6.1.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_50_mInAtimino_50"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_50_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mInAtiminotidINAM lyapi ca",
    text_dev              = "मीनातिमिनोतिदीङां ल्यपि च",
    padaccheda_dev        = "मीनाति-मिनोति-दीङाम् ल्यपि च",
    why_dev               = "(सूत्रम् 6.1.50) मीनातिमिनोतिदीङां ल्यपि च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
