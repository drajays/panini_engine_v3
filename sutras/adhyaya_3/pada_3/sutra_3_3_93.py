"""
3.3.93  कर्मण्यधिकरणे च  —  VIDHI

Padaccheda: कर्मणि अधिकरणे च

krt-suffix rule: कर्मण्यधिकरणे च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_93_karmaRyaDi_93"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_93_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.93"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRyaDikaraRe ca",
    text_dev              = "कर्मण्यधिकरणे च",
    padaccheda_dev        = "कर्मणि अधिकरणे च",
    why_dev               = "धातोः प्रत्ययः (३.3.93)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
