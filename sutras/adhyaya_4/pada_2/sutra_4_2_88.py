"""
4.2.88  नडशादाड्ड्वलच्  —  VIDHI

Padaccheda: नड-शादात् ड्वलच्

नडशादाड्ड्वलच् (4.2.88)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_88_naqaSAdAqq_88"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_88_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naqaSAdAqqvalac",
    text_dev              = "नडशादाड्ड्वलच्",
    padaccheda_dev        = "नड-शादात् ड्वलच्",
    why_dev               = "(सूत्रम् 4.2.88) नडशादाड्ड्वलच्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
