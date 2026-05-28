"""
6.1.91  उपसर्गादृति धातौ  —  VIDHI

Padaccheda: उपसर्गात् ऋति धातौ

उपसर्गादृति धातौ (6.1.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_91_upasargAdf_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargAdfti DAtau",
    text_dev              = "उपसर्गादृति धातौ",
    padaccheda_dev        = "उपसर्गात् ऋति धातौ",
    why_dev               = "(सूत्रम् 6.1.91) उपसर्गादृति धातौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
