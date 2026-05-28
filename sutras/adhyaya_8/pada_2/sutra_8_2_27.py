"""
8.2.27  ह्रस्वादङ्गात्  —  VIDHI

Padaccheda: ह्रस्वात् अङ्गात्

ह्रस्वादङ्गात् (8.2.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_27_hrasvAdaNg_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hrasvAdaNgAt",
    text_dev              = "ह्रस्वादङ्गात्",
    padaccheda_dev        = "ह्रस्वात् अङ्गात्",
    why_dev               = "(सूत्रम् 8.2.27) ह्रस्वादङ्गात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
