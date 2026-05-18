"""
4.1.126  कल्याण्यादीनामिनङ्  —  VIDHI

Padaccheda: कल्याणी-आदीनाम् इनङ्

कल्याण्यादीनामिनङ् (4.1.126)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_126_kalyARyAdI_126"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_126_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.126"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kalyARyAdInAminaN",
    text_dev              = "कल्याण्यादीनामिनङ्",
    padaccheda_dev        = "कल्याणी-आदीनाम् इनङ्",
    why_dev               = "(सूत्रम् 4.1.126) कल्याण्यादीनामिनङ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
