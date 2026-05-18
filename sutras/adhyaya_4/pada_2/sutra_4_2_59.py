"""
4.2.59  तदधीते तद्वेद  —  VIDHI

Padaccheda: तत् अधीते (क्रियापदम्) तद्वेद

तदधीते तद्वेद (4.2.59)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_59_tadaDIte_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_59_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadaDIte tadveda",
    text_dev              = "तदधीते तद्वेद",
    padaccheda_dev        = "तत् अधीते (क्रियापदम्) तद्वेद",
    why_dev               = "(सूत्रम् 4.2.59) तदधीते तद्वेद।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
