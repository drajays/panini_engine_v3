"""
3.2.28  एजेः खश्  —  VIDHI

Padaccheda: एजेः खश्

krt-suffix rule: एजेः खश् (28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_28_ejeH_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ejeH KaS",
    text_dev              = "एजेः खश्",
    padaccheda_dev        = "एजेः खश्",
    why_dev               = "धातोः कृत्-प्रत्ययः [एजेः खश्] विहितः (३.२.28)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
