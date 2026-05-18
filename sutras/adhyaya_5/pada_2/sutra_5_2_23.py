"""
5.2.23  हैयंगवीनं संज्ञायाम्  —  VIDHI

Padaccheda: हैयङ्गवीनम् संज्ञायाम्

हैयंगवीनं संज्ञायाम् (5.2.23)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_23_hEyaMgavIn_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_23_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hEyaMgavInaM saMjYAyAm",
    text_dev              = "हैयंगवीनं संज्ञायाम्",
    padaccheda_dev        = "हैयङ्गवीनम् संज्ञायाम्",
    why_dev               = "(सूत्रम् 5.2.23) हैयंगवीनं संज्ञायाम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
