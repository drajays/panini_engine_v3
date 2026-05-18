"""
4.2.90  उत्करादिभ्यश्छः  —  VIDHI

Padaccheda: उत्कर-आदिभ्यः छः

उत्करादिभ्यश्छः (4.2.90)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_90_utkarAdiBy_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_90_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "utkarAdiByaSCaH",
    text_dev              = "उत्करादिभ्यश्छः",
    padaccheda_dev        = "उत्कर-आदिभ्यः छः",
    why_dev               = "(सूत्रम् 4.2.90) उत्करादिभ्यश्छः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
