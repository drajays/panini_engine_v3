"""
8.3.110  न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम्  —  VIDHI

Padaccheda: न र-पर-सृपि-सृजि-स्पृशि-स्पृहि-सवन-आदीनाम्

न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम् (8.3.110)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_110_na_110"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_110_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na raparasfpisfjispfSispfhisavanAdInAm",
    text_dev              = "न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम्",
    padaccheda_dev        = "न र-पर-सृपि-सृजि-स्पृशि-स्पृहि-सवन-आदीनाम्",
    why_dev               = "(सूत्रम् 8.3.110) न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
