"""
8.4.22  हन्तेरत्पूर्वस्य  —  VIDHI

Padaccheda: हन्तेः अत्-पूर्वस्य

हन्तेरत्पूर्वस्य (8.4.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_22_hanteratpU_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_22_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hanteratpUrvasya",
    text_dev              = "हन्तेरत्पूर्वस्य",
    padaccheda_dev        = "हन्तेः अत्-पूर्वस्य",
    why_dev               = "(सूत्रम् 8.4.22) हन्तेरत्पूर्वस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
