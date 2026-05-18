"""
6.2.25  श्रज्याऽवमकन्पापवत्सु भावे कर्मधारये  —  VIDHI

Padaccheda: श्र-ज्या-अवम-कन्-पापवत्सु भावे कर्मधारये

श्रज्याऽवमकन्पापवत्सु भावे कर्मधारये (6.2.25)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_25_SrajyAvam_25"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_25_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SrajyA'vamakanpApavatsu BAve karmaDAraye",
    text_dev              = "श्रज्याऽवमकन्पापवत्सु भावे कर्मधारये",
    padaccheda_dev        = "श्र-ज्या-अवम-कन्-पापवत्सु भावे कर्मधारये",
    why_dev               = "(सूत्रम् 6.2.25) श्रज्याऽवमकन्पापवत्सु भावे कर्मधारये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
