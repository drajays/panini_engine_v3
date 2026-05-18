"""
8.3.111  सात्पदाद्योः  —  VIDHI

Padaccheda: सात्-पद-आद्योः

सात्पदाद्योः (8.3.111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_111_sAtpadAdyo_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_111_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sAtpadAdyoH",
    text_dev              = "सात्पदाद्योः",
    padaccheda_dev        = "सात्-पद-आद्योः",
    why_dev               = "(सूत्रम् 8.3.111) सात्पदाद्योः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
