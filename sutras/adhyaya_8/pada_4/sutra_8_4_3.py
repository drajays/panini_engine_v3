"""
8.4.3  पूर्वपदात् संज्ञायामगः  —  VIDHI

Padaccheda: पूर्व-पदात् संज्ञायाम् अ-गः

पूर्वपदात् संज्ञायामगः (8.4.3)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_3_pUrvapadAt_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_3_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvapadAt saMjYAyAmagaH",
    text_dev              = "पूर्वपदात् संज्ञायामगः",
    padaccheda_dev        = "पूर्व-पदात् संज्ञायाम् अ-गः",
    why_dev               = "(सूत्रम् 8.4.3) पूर्वपदात् संज्ञायामगः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
