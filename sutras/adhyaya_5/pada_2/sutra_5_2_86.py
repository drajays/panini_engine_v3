"""
5.2.86  पूर्वादिनिः  —  VIDHI

Padaccheda: पूर्वात् इनिः

पूर्वादिनिः (5.2.86)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_86_pUrvAdiniH_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_86_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvAdiniH",
    text_dev              = "पूर्वादिनिः",
    padaccheda_dev        = "पूर्वात् इनिः",
    why_dev               = "(सूत्रम् 5.2.86) पूर्वादिनिः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
