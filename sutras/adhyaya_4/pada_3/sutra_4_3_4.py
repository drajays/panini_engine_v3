"""
4.3.4  अर्धाद्यत्  —  VIDHI

Padaccheda: अर्धात् यत्

अर्धाद्यत् (4.3.4)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_4_arDAdyat_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_4_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arDAdyat",
    text_dev              = "अर्धाद्यत्",
    padaccheda_dev        = "अर्धात् यत्",
    why_dev               = "(सूत्रम् 4.3.4) अर्धाद्यत्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
