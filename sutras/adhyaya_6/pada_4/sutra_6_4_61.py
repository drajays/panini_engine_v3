"""
6.4.61  वाऽऽक्रोशदैन्ययोः  —  VIDHI

Padaccheda: वा आक्रोश-दैन्ययोः

वाऽऽक्रोशदैन्ययोः (6.4.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_61_vAkroSad_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA''kroSadEnyayoH",
    text_dev              = "वाऽऽक्रोशदैन्ययोः",
    padaccheda_dev        = "वा आक्रोश-दैन्ययोः",
    why_dev               = "(सूत्रम् 6.4.61) वाऽऽक्रोशदैन्ययोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
