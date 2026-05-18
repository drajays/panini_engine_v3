"""
3.3.100  कृञः श च  —  VIDHI

Padaccheda: कृञः श (लुप्तप्रथमान्तनिर्देशः) च

krt-suffix rule: कृञः श च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_100_kfYaH_100"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_100_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfYaH Sa ca",
    text_dev              = "कृञः श च",
    padaccheda_dev        = "कृञः श (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "धातोः प्रत्ययः (३.3.100)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
