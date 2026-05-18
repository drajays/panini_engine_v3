"""
4.2.26  शुक्राद्घन्  —  VIDHI

Padaccheda: शुक्रात् घन्

शुक्राद्घन् (4.2.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_26_SukrAdGan_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_26_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SukrAdGan",
    text_dev              = "शुक्राद्घन्",
    padaccheda_dev        = "शुक्रात् घन्",
    why_dev               = "(सूत्रम् 4.2.26) शुक्राद्घन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
