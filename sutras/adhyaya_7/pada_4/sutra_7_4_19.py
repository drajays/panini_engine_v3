"""
7.4.19  पतः पुम्  —  VIDHI

Padaccheda: पतः पुम्

पतः पुम् (7.4.19)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_19_pataH_19"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_19_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pataH pum",
    text_dev              = "पतः पुम्",
    padaccheda_dev        = "पतः पुम्",
    why_dev               = "(सूत्रम् 7.4.19) पतः पुम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
