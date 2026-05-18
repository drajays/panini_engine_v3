"""
6.3.104  का पथ्यक्षयोः  —  VIDHI

Padaccheda: का (लुप्तप्रथमान्तनिर्देशः) पथि-अक्षयोः

का पथ्यक्षयोः (6.3.104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_104_kA_104"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_104_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kA paTyakzayoH",
    text_dev              = "का पथ्यक्षयोः",
    padaccheda_dev        = "का (लुप्तप्रथमान्तनिर्देशः) पथि-अक्षयोः",
    why_dev               = "(सूत्रम् 6.3.104) का पथ्यक्षयोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
