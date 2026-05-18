"""
5.3.36  दक्षिणादाच्  —  VIDHI

Padaccheda: दक्षिणात् आच्

दक्षिणादाच् (5.3.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_36_dakziRAdAc_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_36_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dakziRAdAc",
    text_dev              = "दक्षिणादाच्",
    padaccheda_dev        = "दक्षिणात् आच्",
    why_dev               = "(सूत्रम् 5.3.36) दक्षिणादाच्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
