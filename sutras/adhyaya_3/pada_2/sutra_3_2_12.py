"""
3.2.12  अर्हः  —  VIDHI

Padaccheda: अर्हः

krt-suffix rule: अर्हः (12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_12_arhaH_12"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_12_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arhaH",
    text_dev              = "अर्हः",
    padaccheda_dev        = "अर्हः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अर्हः] विहितः (३.२.12)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
