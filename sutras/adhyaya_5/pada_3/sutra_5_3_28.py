"""
5.3.28  दक्षिणोत्तराभ्यामतसुच्  —  VIDHI

Padaccheda: दक्षिणा-उत्तराभ्याम् अतसुच्

दक्षिणोत्तराभ्यामतसुच् (5.3.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_28_dakziRotta_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_28_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dakziRottarAByAmatasuc",
    text_dev              = "दक्षिणोत्तराभ्यामतसुच्",
    padaccheda_dev        = "दक्षिणा-उत्तराभ्याम् अतसुच्",
    why_dev               = "(सूत्रम् 5.3.28) दक्षिणोत्तराभ्यामतसुच्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
