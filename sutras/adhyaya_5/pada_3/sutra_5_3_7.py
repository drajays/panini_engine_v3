"""
5.3.7  पञ्चम्यास्तसिल्  —  VIDHI

Padaccheda: पञ्चम्याः तसिल्

पञ्चम्यास्तसिल् (5.3.7)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_7_paYcamyAst_7"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_7_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paYcamyAstasil",
    text_dev              = "पञ्चम्यास्तसिल्",
    padaccheda_dev        = "पञ्चम्याः तसिल्",
    why_dev               = "(सूत्रम् 5.3.7) पञ्चम्यास्तसिल्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
