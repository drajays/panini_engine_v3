"""
5.3.91  वत्सोक्षाश्वर्षभेभ्यश्च तनुत्वे  —  VIDHI

Padaccheda: वत्स-उक्ष-अश्व-ऋषभेभ्यः च तनुत्वे

वत्सोक्षाश्वर्षभेभ्यश्च तनुत्वे (5.3.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_91_vatsokzASv_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_91_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vatsokzASvarzaBeByaSca tanutve",
    text_dev              = "वत्सोक्षाश्वर्षभेभ्यश्च तनुत्वे",
    padaccheda_dev        = "वत्स-उक्ष-अश्व-ऋषभेभ्यः च तनुत्वे",
    why_dev               = "(सूत्रम् 5.3.91) वत्सोक्षाश्वर्षभेभ्यश्च तनुत्वे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
