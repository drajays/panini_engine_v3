"""
6.1.154  मस्करमस्करिणौ वेणुपरिव्राजकयोः  —  VIDHI

Padaccheda: मस्कर-मस्करिणौ वेणु-परिव्राजकयोः

मस्करमस्करिणौ वेणुपरिव्राजकयोः (6.1.154)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_154_maskaramas_154"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_154_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.154"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.154",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "maskaramaskariRO veRuparivrAjakayoH",
    text_dev              = "मस्करमस्करिणौ वेणुपरिव्राजकयोः",
    padaccheda_dev        = "मस्कर-मस्करिणौ वेणु-परिव्राजकयोः",
    why_dev               = "(सूत्रम् 6.1.154) मस्करमस्करिणौ वेणुपरिव्राजकयोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
