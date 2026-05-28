"""
8.2.67  अवयाःश्वेतवाःपुरोडाश्च  —  VIDHI

Padaccheda: अवयाः श्वेतवाः पुरोडाः च

अवयाःश्वेतवाःपुरोडाश्च (8.2.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_67_avayAHSvet_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avayAHSvetavAHpuroqASca",
    text_dev              = "अवयाःश्वेतवाःपुरोडाश्च",
    padaccheda_dev        = "अवयाः श्वेतवाः पुरोडाः च",
    why_dev               = "(सूत्रम् 8.2.67) अवयाःश्वेतवाःपुरोडाश्च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
