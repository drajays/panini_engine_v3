"""
6.3.125  अष्टनः संज्ञायाम्  —  VIDHI

Padaccheda: अष्टनः संज्ञायाम्

अष्टनः संज्ञायाम् (6.3.125)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_125_azwanaH_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_125_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "azwanaH saMjYAyAm",
    text_dev              = "अष्टनः संज्ञायाम्",
    padaccheda_dev        = "अष्टनः संज्ञायाम्",
    why_dev               = "(सूत्रम् 6.3.125) अष्टनः संज्ञायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
