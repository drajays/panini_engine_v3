"""
4.1.127  कुलटाया वा  —  VIDHI

Padaccheda: कुलटायाः वा

कुलटाया वा (4.1.127)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_127_kulawAyA_127"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_127_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kulawAyA vA",
    text_dev              = "कुलटाया वा",
    padaccheda_dev        = "कुलटायाः वा",
    why_dev               = "(सूत्रम् 4.1.127) कुलटाया वा।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
