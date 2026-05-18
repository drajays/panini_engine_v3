"""
7.3.32  हनस्तोऽचिण्णलोः  —  VIDHI

Padaccheda: हनः तः अ-चिण्-णलोः

हनस्तोऽचिण्णलोः (7.3.32)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_32_hanastoci_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_32_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hanasto'ciRRaloH",
    text_dev              = "हनस्तोऽचिण्णलोः",
    padaccheda_dev        = "हनः तः अ-चिण्-णलोः",
    why_dev               = "(सूत्रम् 7.3.32) हनस्तोऽचिण्णलोः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
