"""
4.3.31  अ च  —  VIDHI

Padaccheda: अ (लुप्तप्रथमान्तनिर्देशः) च

अ च (4.3.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_31_a_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "a ca",
    text_dev              = "अ च",
    padaccheda_dev        = "अ (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 4.3.31) अ च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
