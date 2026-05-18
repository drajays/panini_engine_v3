"""
4.2.98  दक्षिणापश्चात्पुरसस्त्यक्  —  VIDHI

Padaccheda: दक्षिणा-पश्चात्-पुरसः त्यक्

दक्षिणापश्चात्पुरसस्त्यक् (4.2.98)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_98_dakziRApaS_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_98_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dakziRApaScAtpurasastyak",
    text_dev              = "दक्षिणापश्चात्पुरसस्त्यक्",
    padaccheda_dev        = "दक्षिणा-पश्चात्-पुरसः त्यक्",
    why_dev               = "(सूत्रम् 4.2.98) दक्षिणापश्चात्पुरसस्त्यक्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
