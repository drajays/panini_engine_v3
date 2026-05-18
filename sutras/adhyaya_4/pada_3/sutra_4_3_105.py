"""
4.3.105  पुराणप्रोक्तेषु ब्राह्मणकल्पेषु  —  VIDHI

Padaccheda: पुराणप्रोक्तेषु ब्राह्मणकल्पेषु

पुराणप्रोक्तेषु ब्राह्मणकल्पेषु (4.3.105)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_105_purARaprok_105"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_105_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "purARaproktezu brAhmaRakalpezu",
    text_dev              = "पुराणप्रोक्तेषु ब्राह्मणकल्पेषु",
    padaccheda_dev        = "पुराणप्रोक्तेषु ब्राह्मणकल्पेषु",
    why_dev               = "(सूत्रम् 4.3.105) पुराणप्रोक्तेषु ब्राह्मणकल्पेषु।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
