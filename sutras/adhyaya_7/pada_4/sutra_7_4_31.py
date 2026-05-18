"""
7.4.31  ई घ्राध्मोः  —  VIDHI

Padaccheda: ई (लुप्तप्रथमान्तनिर्देशः) घ्रा-ध्मोः

ई घ्राध्मोः (7.4.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_31_I_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "I GrADmoH",
    text_dev              = "ई घ्राध्मोः",
    padaccheda_dev        = "ई (लुप्तप्रथमान्तनिर्देशः) घ्रा-ध्मोः",
    why_dev               = "(सूत्रम् 7.4.31) ई घ्राध्मोः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
