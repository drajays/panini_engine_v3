"""
5.2.31  नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्राटचः  —  VIDHI

Padaccheda: नते नासिकायाः संज्ञायाम् टीटच्-नाटच्-भ्रटचः

नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्राटचः (5.2.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_31_nate_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nate nAsikAyAH saMjYAyAM wIwaYnAwajBrAwacaH",
    text_dev              = "नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्राटचः",
    padaccheda_dev        = "नते नासिकायाः संज्ञायाम् टीटच्-नाटच्-भ्रटचः",
    why_dev               = "(सूत्रम् 5.2.31) नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्राटचः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
