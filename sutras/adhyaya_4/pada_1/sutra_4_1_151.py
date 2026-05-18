"""
4.1.151  कुर्वादिभ्यो ण्यः  —  VIDHI

Padaccheda: कुरु-आदिभ्यः ण्यः

कुर्वादिभ्यो ण्यः (4.1.151)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_151_kurvAdiByo_151"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_151_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.151"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.151",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kurvAdiByo RyaH",
    text_dev              = "कुर्वादिभ्यो ण्यः",
    padaccheda_dev        = "कुरु-आदिभ्यः ण्यः",
    why_dev               = "(सूत्रम् 4.1.151) कुर्वादिभ्यो ण्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
