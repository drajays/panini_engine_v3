"""
8.1.24  न चवाहाहैवयुक्ते  —  VIDHI

Padaccheda: न च-वा-ह-अह-एव-युक्ते

न चवाहाहैवयुक्ते (8.1.24)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_24_na_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_24_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na cavAhAhEvayukte",
    text_dev              = "न चवाहाहैवयुक्ते",
    padaccheda_dev        = "न च-वा-ह-अह-एव-युक्ते",
    why_dev               = "(सूत्रम् 8.1.24) न चवाहाहैवयुक्ते।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
