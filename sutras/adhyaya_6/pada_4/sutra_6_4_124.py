"""
6.4.124  वा जॄभ्रमुत्रसाम्  —  VIDHI

Padaccheda: वा जॄ-भ्रमु-त्रसाम्

वा जॄभ्रमुत्रसाम् (6.4.124)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_124_vA_124"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_124_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA jFBramutrasAm",
    text_dev              = "वा जॄभ्रमुत्रसाम्",
    padaccheda_dev        = "वा जॄ-भ्रमु-त्रसाम्",
    why_dev               = "(सूत्रम् 6.4.124) वा जॄभ्रमुत्रसाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
