"""
8.3.43  द्विस्त्रिश्चतुरिति कृत्वोऽर्थे  —  VIDHI

Padaccheda: द्विस् · त्रिस् · चतुस् · इति · कृत्वोऽर्थे

द्विस्त्रिश्चतुरिति कृत्वोऽर्थे (8.3.43)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_43_dvistriSca_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_43_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvistriScaturiti kftvo'rTe",
    text_dev              = "द्विस्त्रिश्चतुरिति कृत्वोऽर्थे",
    padaccheda_dev        = "द्विस् · त्रिस् · चतुस् · इति · कृत्वोऽर्थे",
    why_dev               = "(सूत्रम् 8.3.43) द्विस्त्रिश्चतुरिति कृत्वोऽर्थे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
