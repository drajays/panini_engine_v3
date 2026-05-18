"""
3.4.61  स्वाङ्गे तस्प्रत्यये कृभ्वोः  —  VIDHI

Padaccheda: स्वाङ्गे तस्-प्रत्यये कृ-भ्वोः

krt-suffix rule: स्वाङ्गे तस्प्रत्यये कृभ्वोः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_61_svANge_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svANge taspratyaye kfBvoH",
    text_dev              = "स्वाङ्गे तस्प्रत्यये कृभ्वोः",
    padaccheda_dev        = "स्वाङ्गे तस्-प्रत्यये कृ-भ्वोः",
    why_dev               = "धातोः प्रत्ययः (३.4.61)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
