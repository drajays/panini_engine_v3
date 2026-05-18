"""
5.3.111  प्रत्नपूर्वविश्वेमात्थाल् छन्दसि  —  VIDHI

Padaccheda: प्रत्न-पूर्व-विश्व-इमात् थाल् छन्दसि

प्रत्नपूर्वविश्वेमात्थाल् छन्दसि (5.3.111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_111_pratnapUrv_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_111_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratnapUrvaviSvemAtTAl Candasi",
    text_dev              = "प्रत्नपूर्वविश्वेमात्थाल् छन्दसि",
    padaccheda_dev        = "प्रत्न-पूर्व-विश्व-इमात् थाल् छन्दसि",
    why_dev               = "(सूत्रम् 5.3.111) प्रत्नपूर्वविश्वेमात्थाल् छन्दसि।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
