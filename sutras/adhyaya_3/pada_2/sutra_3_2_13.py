"""
3.2.13  स्तम्बकर्णयोः रमिजपोः  —  VIDHI

Padaccheda: स्तम्ब-कर्णयोः रमि-जपोः

krt-suffix rule: स्तम्बकर्णयोः रमिजपोः (13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_13_stambakarR_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_13_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stambakarRayoH ramijapoH",
    text_dev              = "स्तम्बकर्णयोः रमिजपोः",
    padaccheda_dev        = "स्तम्ब-कर्णयोः रमि-जपोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्तम्बकर्णयोः रमिजपोः] विहितः (३.२.13)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
