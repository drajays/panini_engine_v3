"""
4.3.139  ओरञ्  —  VIDHI

Padaccheda: ओः अञ्

ओरञ् (4.3.139)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_139_oraY_139"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_139_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.139"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.139",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "oraY",
    text_dev              = "ओरञ्",
    padaccheda_dev        = "ओः अञ्",
    why_dev               = "(सूत्रम् 4.3.139) ओरञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
