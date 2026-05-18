"""
6.3.81  अव्ययीभावे चाकाले  —  VIDHI

Padaccheda: अव्ययीभावे च अकाले

अव्ययीभावे चाकाले (6.3.81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_81_avyayIBAve_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_81_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avyayIBAve cAkAle",
    text_dev              = "अव्ययीभावे चाकाले",
    padaccheda_dev        = "अव्ययीभावे च अकाले",
    why_dev               = "(सूत्रम् 6.3.81) अव्ययीभावे चाकाले।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
