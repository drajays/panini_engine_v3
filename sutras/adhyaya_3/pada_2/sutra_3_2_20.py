"""
3.2.20  कृञो हेतुताच्छील्यानुलोम्येषु  —  VIDHI

Padaccheda: कृञः हेतु-ताच्छील्य-आनुलोम्येषु

krt-suffix rule: कृञो हेतुताच्छील्यानुलोम्येषु (20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_20_kfYo_20"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfYo hetutAcCIlyAnulomyezu",
    text_dev              = "कृञो हेतुताच्छील्यानुलोम्येषु",
    padaccheda_dev        = "कृञः हेतु-ताच्छील्य-आनुलोम्येषु",
    why_dev               = "धातोः कृत्-प्रत्ययः [कृञो हेतुताच्छील्यानुलोम्येषु] विहितः (३.२.20)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
