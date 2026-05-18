"""
8.3.29  डः सि धुट्  —  VIDHI

Padaccheda: डः सि धुट्

डः सि धुट् (8.3.29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_29_qaH_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_29_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "qaH si Duw",
    text_dev              = "डः सि धुट्",
    padaccheda_dev        = "डः सि धुट्",
    why_dev               = "(सूत्रम् 8.3.29) डः सि धुट्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
