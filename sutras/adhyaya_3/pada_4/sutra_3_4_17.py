"""
3.4.17  सृपितृदोः कसुन्  —  VIDHI

Padaccheda: सृपि-तृदोः कसुन्

krt-suffix rule: सृपितृदोः कसुन्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_17_sfpitfdoH_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("3_4_17_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sfpitfdoH kasun",
    text_dev              = "सृपितृदोः कसुन्",
    padaccheda_dev        = "सृपि-तृदोः कसुन्",
    why_dev               = "धातोः प्रत्ययः (३.4.17)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
