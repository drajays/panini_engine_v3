"""
4.1.171  वृद्धेत्कोसलाजादाञ्ञ्यङ्  —  VIDHI

Padaccheda: वृद्ध-इत्-कोसल-आजादात् ञ्यङ्

वृद्धेत्कोसलाजादाञ्ञ्यङ् (4.1.171)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_171_vfdDetkosa_171"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_171_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.171"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.171",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vfdDetkosalAjAdAYYyaN",
    text_dev              = "वृद्धेत्कोसलाजादाञ्ञ्यङ्",
    padaccheda_dev        = "वृद्ध-इत्-कोसल-आजादात् ञ्यङ्",
    why_dev               = "(सूत्रम् 4.1.171) वृद्धेत्कोसलाजादाञ्ञ्यङ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
