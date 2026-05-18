"""
4.3.64  अशब्दे यत्खावन्यतरस्याम्  —  VIDHI

Padaccheda: अशब्दे यत्-खौ अन्यतरस्याम्

अशब्दे यत्खावन्यतरस्याम् (4.3.64)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_64_aSabde_64"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_64_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aSabde yatKAvanyatarasyAm",
    text_dev              = "अशब्दे यत्खावन्यतरस्याम्",
    padaccheda_dev        = "अशब्दे यत्-खौ अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 4.3.64) अशब्दे यत्खावन्यतरस्याम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
