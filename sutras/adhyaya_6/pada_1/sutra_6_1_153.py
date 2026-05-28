"""
6.1.153  प्रस्कण्वहरिश्चन्द्रावृषी  —  VIDHI

Padaccheda: प्रस्कण्व-हरिश्चन्द्रौ ऋषी

प्रस्कण्वहरिश्चन्द्रावृषी (6.1.153)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_153_praskaRvah_153"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.153"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.153",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "praskaRvahariScandrAvfzI",
    text_dev              = "प्रस्कण्वहरिश्चन्द्रावृषी",
    padaccheda_dev        = "प्रस्कण्व-हरिश्चन्द्रौ ऋषी",
    why_dev               = "(सूत्रम् 6.1.153) प्रस्कण्वहरिश्चन्द्रावृषी।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
