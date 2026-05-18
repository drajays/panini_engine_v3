"""
4.1.91  फक्फिञोरन्यतरस्याम्  —  VIDHI

Padaccheda: फक्-फिञोः अन्यतरस्याम्

फक्फिञोरन्यतरस्याम् (4.1.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_91_PakPiYoran_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_91_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "PakPiYoranyatarasyAm",
    text_dev              = "फक्फिञोरन्यतरस्याम्",
    padaccheda_dev        = "फक्-फिञोः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 4.1.91) फक्फिञोरन्यतरस्याम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
