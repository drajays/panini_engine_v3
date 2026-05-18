"""
6.4.170  न मपूर्वोऽपत्येऽवर्मणः  —  VIDHI

Padaccheda: न म-पूर्वः अपत्ये अवर्मणः

न मपूर्वोऽपत्येऽवर्मणः (6.4.170)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_170_na_170"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_170_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.170"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.170",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na mapUrvo'patye'varmaRaH",
    text_dev              = "न मपूर्वोऽपत्येऽवर्मणः",
    padaccheda_dev        = "न म-पूर्वः अपत्ये अवर्मणः",
    why_dev               = "(सूत्रम् 6.4.170) न मपूर्वोऽपत्येऽवर्मणः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
