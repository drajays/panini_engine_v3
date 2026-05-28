"""
6.1.188  स्वपादिर्हिंसामच्यनिटि  —  VIDHI

Padaccheda: स्वप्-आदि-र्हिंसाम् अचि अन्-इटि

स्वपादिर्हिंसामच्यनिटि (6.1.188)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_188_svapAdirhi_188"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_188_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.188"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.188",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svapAdirhiMsAmacyaniwi",
    text_dev              = "स्वपादिर्हिंसामच्यनिटि",
    padaccheda_dev        = "स्वप्-आदि-र्हिंसाम् अचि अन्-इटि",
    why_dev               = "(सूत्रम् 6.1.188) स्वपादिर्हिंसामच्यनिटि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
