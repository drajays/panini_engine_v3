"""
5.4.49  रोगाच्चापनयने  —  VIDHI

Padaccheda: रोगात् च अपनयने

रोगाच्चापनयने (5.4.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_49_rogAccApan_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_49_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rogAccApanayane",
    text_dev              = "रोगाच्चापनयने",
    padaccheda_dev        = "रोगात् च अपनयने",
    why_dev               = "(सूत्रम् 5.4.49) रोगाच्चापनयने।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
