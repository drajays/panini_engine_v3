"""
2.4.31  अर्धर्चाः पुंसि च  —  VIDHI

Padaccheda: अर्धर्चाः पुंसि च

ardharca words are also masculine.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_31_ardharca_pumsi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arDarcAH puMsi ca",
    text_dev              = "अर्धर्चाः पुंसि च",
    padaccheda_dev        = "अर्धर्चाः पुंसि च",
    why_dev               = "अर्धर्चाः पुंसि च (२.४.३१)।",
    anuvritti_from        = ('2.4.26',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
