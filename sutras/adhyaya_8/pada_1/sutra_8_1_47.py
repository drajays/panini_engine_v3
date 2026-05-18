"""
8.1.47  जात्वपूर्वम्  —  VIDHI

Padaccheda: जातु अ-पूर्वम्

जात्वपूर्वम् (8.1.47)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_47_jAtvapUrva_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_47_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAtvapUrvam",
    text_dev              = "जात्वपूर्वम्",
    padaccheda_dev        = "जातु अ-पूर्वम्",
    why_dev               = "(सूत्रम् 8.1.47) जात्वपूर्वम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
