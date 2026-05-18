"""
2.4.29  रात्राह्नाहाः पुंसि  —  VIDHI

Padaccheda: रात्र-अह्न-अहाः पुंसि

raatri, ahna, aha are masculine in compounds.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_29_ratra_ahna"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_29_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAtrAhnAhAH puMsi",
    text_dev              = "रात्राह्नाहाः पुंसि",
    padaccheda_dev        = "रात्र-अह्न-अहाः पुंसि",
    why_dev               = "रात्र-अह्न-अहाः पुंसि (२.४.२९)।",
    anuvritti_from        = ('2.4.26',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
