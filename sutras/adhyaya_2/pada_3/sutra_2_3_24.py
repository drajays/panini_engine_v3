"""
2.3.24  अकर्तर्यृणे पञ्चमी  —  VIDHI

Padaccheda: अ-कर्तरि ऋणे पञ्चमी

Pancami marks debt when not from the agent.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_24_akartari_rne"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_24_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "akartaryfRe paYcamI",
    text_dev              = "अकर्तर्यृणे पञ्चमी",
    padaccheda_dev        = "अ-कर्तरि ऋणे पञ्चमी",
    why_dev               = "अ-कर्तरि ऋणे पञ्चमी (२.३.२४)।",
    anuvritti_from        = ('2.3.28',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
