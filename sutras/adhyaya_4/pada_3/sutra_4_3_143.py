"""
4.3.143  मयड्वैतयोर्भाषायामभक्ष्याच्छादनयोः  —  VIDHI

Padaccheda: मयट् वा एतयोः भाषायाम् अभक्ष्य-आच्छादनयोः

मयड्वैतयोर्भाषायामभक्ष्याच्छादनयोः (4.3.143)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_143_mayaqvEtay_143"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_143_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.143"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.143",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mayaqvEtayorBAzAyAmaBakzyAcCAdanayoH",
    text_dev              = "मयड्वैतयोर्भाषायामभक्ष्याच्छादनयोः",
    padaccheda_dev        = "मयट् वा एतयोः भाषायाम् अभक्ष्य-आच्छादनयोः",
    why_dev               = "(सूत्रम् 4.3.143) मयड्वैतयोर्भाषायामभक्ष्याच्छादनयोः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
