"""
6.3.115  कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य  —  VIDHI

Padaccheda: कर्णे लक्षणस्य अ-विष्ट-अष्ट-पञ्च-मणि-भिन्न-छिन्न-छिद्र-स्रुव-स्वस्तिकस्य

कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य (6.3.115)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_115_karRe_115"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_115_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karRe lakzaRasyAvizwAzwapaYcamaRiBinnaCinnaCidrasruvasvastikasya",
    text_dev              = "कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य",
    padaccheda_dev        = "कर्णे लक्षणस्य अ-विष्ट-अष्ट-पञ्च-मणि-भिन्न-छिन्न-छिद्र-स्रुव-स्वस्तिकस्य",
    why_dev               = "(सूत्रम् 6.3.115) कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
