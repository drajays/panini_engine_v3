"""
7.4.34  अशनायोदन्यधनाया बुभुक्षापिपासागर्द्धेषु  —  VIDHI

Padaccheda: अशनाय-उदन्य-धनाया बुभुक्षा-पिपासा-गर्द्धेषु

अशनायोदन्यधनाया बुभुक्षापिपासागर्द्धेषु (7.4.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_34_aSanAyodan_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_34_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aSanAyodanyaDanAyA buBukzApipAsAgardDezu",
    text_dev              = "अशनायोदन्यधनाया बुभुक्षापिपासागर्द्धेषु",
    padaccheda_dev        = "अशनाय-उदन्य-धनाया बुभुक्षा-पिपासा-गर्द्धेषु",
    why_dev               = "(सूत्रम् 7.4.34) अशनायोदन्यधनाया बुभुक्षापिपासागर्द्धेषु।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
