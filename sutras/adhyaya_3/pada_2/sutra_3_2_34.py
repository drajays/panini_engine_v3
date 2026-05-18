"""
3.2.34  मितनखे च  —  VIDHI

Padaccheda: मित-नखे च

krt-suffix rule: मितनखे च (34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_34_mitanaKe_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_34_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mitanaKe ca",
    text_dev              = "मितनखे च",
    padaccheda_dev        = "मित-नखे च",
    why_dev               = "धातोः कृत्-प्रत्ययः [मितनखे च] विहितः (३.२.34)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
