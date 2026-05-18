"""
5.2.69  अंशं हारी  —  VIDHI

Padaccheda: अंशम् हारी

अंशं हारी (5.2.69)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_69_aMSaM_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_69_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aMSaM hArI",
    text_dev              = "अंशं हारी",
    padaccheda_dev        = "अंशम् हारी",
    why_dev               = "(सूत्रम् 5.2.69) अंशं हारी।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
