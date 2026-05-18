"""
3.4.25  कर्मण्याक्रोशे कृञः खमुञ्  —  VIDHI

Padaccheda: कर्मणि आक्रोशे कृञः खमुञ्

krt-suffix rule: कर्मण्याक्रोशे कृञः खमुञ्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_25_karmaRyAkr_25"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_25_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRyAkroSe kfYaH KamuY",
    text_dev              = "कर्मण्याक्रोशे कृञः खमुञ्",
    padaccheda_dev        = "कर्मणि आक्रोशे कृञः खमुञ्",
    why_dev               = "धातोः प्रत्ययः (३.4.25)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
