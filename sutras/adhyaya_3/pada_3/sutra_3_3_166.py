"""
3.3.166  अधीष्टे च  —  VIDHI

Padaccheda: अधीष्टे च

krt-suffix rule: अधीष्टे च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_166_aDIzwe_166"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_166_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.166"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.166",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDIzwe ca",
    text_dev              = "अधीष्टे च",
    padaccheda_dev        = "अधीष्टे च",
    why_dev               = "धातोः प्रत्ययः (३.3.166)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
