"""
4.2.119  ओर्देशे ठञ्  —  VIDHI

Padaccheda: ओः देशे ठञ्

ओर्देशे ठञ् (4.2.119)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_119_ordeSe_119"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_119_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ordeSe WaY",
    text_dev              = "ओर्देशे ठञ्",
    padaccheda_dev        = "ओः देशे ठञ्",
    why_dev               = "(सूत्रम् 4.2.119) ओर्देशे ठञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
