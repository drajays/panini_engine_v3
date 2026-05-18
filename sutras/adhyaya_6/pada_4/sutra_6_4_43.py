"""
6.4.43  ये विभाषा  —  VIDHI

Padaccheda: ये विभाषा

ये विभाषा (6.4.43)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_43_ye_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_43_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ye viBAzA",
    text_dev              = "ये विभाषा",
    padaccheda_dev        = "ये विभाषा",
    why_dev               = "(सूत्रम् 6.4.43) ये विभाषा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
