"""
5.1.8  अजाविभ्यां थ्यन्  —  VIDHI

Padaccheda: अजा-अविभ्याम् थ्यन्

अजाविभ्यां थ्यन् (5.1.8)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_8_ajAviByAM_8"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_8_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ajAviByAM Tyan",
    text_dev              = "अजाविभ्यां थ्यन्",
    padaccheda_dev        = "अजा-अविभ्याम् थ्यन्",
    why_dev               = "(सूत्रम् 5.1.8) अजाविभ्यां थ्यन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
