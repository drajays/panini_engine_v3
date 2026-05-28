"""
7.4.84  नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम्  —  VIDHI

Padaccheda: नीक् वञ्चु-स्रंसु-ध्वंसु-भ्रंसु-कस-पत-पद-स्कन्दाम्

नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम् (7.4.84)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_84_nIgvaYcusr_84"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.84", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.84"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nIgvaYcusraMsuDvaMsuBraMsukasapatapadaskandAm",
    text_dev              = "नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम्",
    padaccheda_dev        = "नीक् वञ्चु-स्रंसु-ध्वंसु-भ्रंसु-कस-पत-पद-स्कन्दाम्",
    why_dev               = "(सूत्रम् 7.4.84) नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
