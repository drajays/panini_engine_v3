"""
4.1.169  साल्वेयगान्धारिभ्यां च  —  VIDHI

Padaccheda: साल्वेय-गान्धारिभ्याम् च

साल्वेयगान्धारिभ्यां च (4.1.169)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_169_sAlveyagAn_169"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_169_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.169"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.169",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sAlveyagAnDAriByAM ca",
    text_dev              = "साल्वेयगान्धारिभ्यां च",
    padaccheda_dev        = "साल्वेय-गान्धारिभ्याम् च",
    why_dev               = "(सूत्रम् 4.1.169) साल्वेयगान्धारिभ्यां च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
