"""
5.2.140  अहंशुभमोर्युस्  —  VIDHI

Padaccheda: अहं-शुभमोः युस्

अहंशुभमोर्युस् (5.2.140)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_140_ahaMSuBamo_140"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_140_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.140"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.140",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ahaMSuBamoryus",
    text_dev              = "अहंशुभमोर्युस्",
    padaccheda_dev        = "अहं-शुभमोः युस्",
    why_dev               = "(सूत्रम् 5.2.140) अहंशुभमोर्युस्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
