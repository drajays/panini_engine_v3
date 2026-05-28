"""
2.3.70  अकेनोर्भविष्यदाधमर्ण्ययोः  —  VIDHI

Padaccheda: अक-इनोः भविष्यत्-आधमर्ण्ययोः

For ak and in suffixes in future/debt context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_70_aka_ina_bhavishya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "akenorBavizyadADamarRyayoH",
    text_dev              = "अकेनोर्भविष्यदाधमर्ण्ययोः",
    padaccheda_dev        = "अक-इनोः भविष्यत्-आधमर्ण्ययोः",
    why_dev               = "अक-इनोः भविष्यत्-आधमर्ण्ययोः (२.३.७०)।",
    anuvritti_from        = ('2.3.65',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
