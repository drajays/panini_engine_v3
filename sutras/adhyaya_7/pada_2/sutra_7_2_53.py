"""
7.2.53  अञ्चेः पूजायाम्  —  VIDHI

Padaccheda: अञ्चेः पूजायाम्

अञ्चेः पूजायाम् (7.2.53)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_53_aYceH_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_53_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aYceH pUjAyAm",
    text_dev              = "अञ्चेः पूजायाम्",
    padaccheda_dev        = "अञ्चेः पूजायाम्",
    why_dev               = "(सूत्रम् 7.2.53) अञ्चेः पूजायाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
