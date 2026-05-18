"""
2.4.58  ण्यक्षत्रियार्षञितो यूनि लुगणिञोः  —  VIDHI

Padaccheda: ण्य-क्षत्रिय-आर्ष-ञितः यूनि लुक् अण्-इञोः

luk of an and ina in nyakshtriya arsha ñit in yuvaka context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_58_nya_ksatriya_yuni"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_58_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "RyakzatriyArzaYito yUni lugaRiYoH",
    text_dev              = "ण्यक्षत्रियार्षञितो यूनि लुगणिञोः",
    padaccheda_dev        = "ण्य-क्षत्रिय-आर्ष-ञितः यूनि लुक् अण्-इञोः",
    why_dev               = "ण्य-क्षत्रिय-आर्ष-ञित्-यूनि लुक् अण्-इञोः (२.४.५८)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
