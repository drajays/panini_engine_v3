"""
3.2.86  कर्मणि हनः  —  VIDHI

Padaccheda: कर्मणि हनः

krt-suffix rule: कर्मणि हनः (86)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_86_karmaRi_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_86_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRi hanaH",
    text_dev              = "कर्मणि हनः",
    padaccheda_dev        = "कर्मणि हनः",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्मणि हनः] विहितः (३.२.86)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
