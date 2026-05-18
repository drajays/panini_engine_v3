"""
6.1.115  प्रकृत्याऽन्तःपादमव्यपरे  —  VIDHI

Padaccheda: प्रकृत्या अन्तःपादम् अ-व्-य-परे

प्रकृत्याऽन्तःपादमव्यपरे (6.1.115)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_115_prakftyAn_115"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_115_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prakftyA'ntaHpAdamavyapare",
    text_dev              = "प्रकृत्याऽन्तःपादमव्यपरे",
    padaccheda_dev        = "प्रकृत्या अन्तःपादम् अ-व्-य-परे",
    why_dev               = "(सूत्रम् 6.1.115) प्रकृत्याऽन्तःपादमव्यपरे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
