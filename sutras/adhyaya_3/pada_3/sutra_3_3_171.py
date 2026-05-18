"""
3.3.171  कृत्याश्च  —  VIDHI

Padaccheda: कृत्याः च

krt-suffix rule: कृत्याश्च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_171_kftyASca_171"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_171_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.171"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.171",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kftyASca",
    text_dev              = "कृत्याश्च",
    padaccheda_dev        = "कृत्याः च",
    why_dev               = "धातोः प्रत्ययः (३.3.171)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
