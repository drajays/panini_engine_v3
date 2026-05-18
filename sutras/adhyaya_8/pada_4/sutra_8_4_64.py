"""
8.4.64  हलो यमां यमि लोपः  —  VIDHI

Padaccheda: हलः यमाम् यमि लोपः

हलो यमां यमि लोपः (8.4.64)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_64_halo_64"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_64_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "halo yamAM yami lopaH",
    text_dev              = "हलो यमां यमि लोपः",
    padaccheda_dev        = "हलः यमाम् यमि लोपः",
    why_dev               = "(सूत्रम् 8.4.64) हलो यमां यमि लोपः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
