"""
2.3.59  विभाषोपसर्गे  —  VIDHI

Padaccheda: विभाषा उपसर्गे

Optional sasthi with upasarga.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_59_upasarga_vibhasa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzopasarge",
    text_dev              = "विभाषोपसर्गे",
    padaccheda_dev        = "विभाषा उपसर्गे",
    why_dev               = "उपसर्गे विभाषा (२.३.५९)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
