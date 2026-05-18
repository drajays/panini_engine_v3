"""
4.3.49  ग्रीष्मावरसमाद्वुञ्  —  VIDHI

Padaccheda: ग्रीष्म-अवरसमात् वुञ्

ग्रीष्मावरसमाद्वुञ् (4.3.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_49_grIzmAvara_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_49_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grIzmAvarasamAdvuY",
    text_dev              = "ग्रीष्मावरसमाद्वुञ्",
    padaccheda_dev        = "ग्रीष्म-अवरसमात् वुञ्",
    why_dev               = "(सूत्रम् 4.3.49) ग्रीष्मावरसमाद्वुञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
