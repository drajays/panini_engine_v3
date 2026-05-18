"""
7.1.75  अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः  —  VIDHI

Padaccheda: अस्थि-दधि-सक्थि-अक्ष्णाम् अनङ् उदात्तः

अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः (7.1.75)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_75_asTidaDisa_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_75_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asTidaDisakTyakzRAmanaNudAttaH",
    text_dev              = "अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः",
    padaccheda_dev        = "अस्थि-दधि-सक्थि-अक्ष्णाम् अनङ् उदात्तः",
    why_dev               = "(सूत्रम् 7.1.75) अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
