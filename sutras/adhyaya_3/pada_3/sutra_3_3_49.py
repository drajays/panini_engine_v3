"""
3.3.49  उदि श्रयतियौतिपूद्रुवः  —  VIDHI

Padaccheda: उदि श्रयति-यौति-पू-द्रुवः

krt-suffix rule: उदि श्रयतियौतिपूद्रुवः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_49_udi_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udi SrayatiyOtipUdruvaH",
    text_dev              = "उदि श्रयतियौतिपूद्रुवः",
    padaccheda_dev        = "उदि श्रयति-यौति-पू-द्रुवः",
    why_dev               = "धातोः प्रत्ययः (३.3.49)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
