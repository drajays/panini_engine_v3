"""
8.2.65  म्वोश्च  —  VIDHI

Padaccheda: म्-वोः च

म्वोश्च (8.2.65)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_65_mvoSca_65"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_65_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mvoSca",
    text_dev              = "म्वोश्च",
    padaccheda_dev        = "म्-वोः च",
    why_dev               = "(सूत्रम् 8.2.65) म्वोश्च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
