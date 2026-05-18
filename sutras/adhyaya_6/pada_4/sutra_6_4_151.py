"""
6.4.151  आपत्यस्य च तद्धितेऽनाति  —  VIDHI

Padaccheda: आपत्यस्य च तद्धिते अन्-आति

आपत्यस्य च तद्धितेऽनाति (6.4.151)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_151_Apatyasya_151"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_151_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.151"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.151",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Apatyasya ca tadDite'nAti",
    text_dev              = "आपत्यस्य च तद्धितेऽनाति",
    padaccheda_dev        = "आपत्यस्य च तद्धिते अन्-आति",
    why_dev               = "(सूत्रम् 6.4.151) आपत्यस्य च तद्धितेऽनाति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
