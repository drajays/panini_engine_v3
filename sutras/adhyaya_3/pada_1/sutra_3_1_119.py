"""
3.1.119  पदास्वैरिबाह्यापक्ष्येषु च  —  VIDHI

Padaccheda: पद-अस्वैरि-बाह्या-पक्ष्येषु च

Krt suffix rule from dhatu: पदास्वैरिबाह्यापक्ष्येषु च (119)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_119_padAsvEribAh_119"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_119_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "padAsvEribAhyApakzyezu ca",
    text_dev              = "पदास्वैरिबाह्यापक्ष्येषु च",
    padaccheda_dev        = "पद-अस्वैरि-बाह्या-पक्ष्येषु च",
    why_dev               = "धातोः [पदास्वैरिबाह्यापक्ष्येषु च]-प्रत्ययः विहितः (३.१.119)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
