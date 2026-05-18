"""
3.2.127  तौ सत्  —  VIDHI

Padaccheda: तौ सत्

krt-suffix rule: तौ सत् (127)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_127_tO_127"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_127_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tO sat",
    text_dev              = "तौ सत्",
    padaccheda_dev        = "तौ सत्",
    why_dev               = "धातोः कृत्-प्रत्ययः [तौ सत्] विहितः (३.२.127)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
