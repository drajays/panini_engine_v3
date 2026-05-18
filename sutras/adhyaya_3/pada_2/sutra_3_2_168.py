"""
3.2.168  सनाशंसभिक्ष उः  —  VIDHI

Padaccheda: सन्-आशंस-भिक्षः उः

krt-suffix rule: सनाशंसभिक्ष उः (168)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_168_sanASaMsaB_168"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_168_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.168"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.168",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sanASaMsaBikza uH",
    text_dev              = "सनाशंसभिक्ष उः",
    padaccheda_dev        = "सन्-आशंस-भिक्षः उः",
    why_dev               = "धातोः कृत्-प्रत्ययः [सनाशंसभिक्ष उः] विहितः (३.२.168)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
