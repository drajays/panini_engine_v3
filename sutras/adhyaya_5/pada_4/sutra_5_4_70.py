"""
5.4.70  किमः क्षेपे  —  VIDHI

Padaccheda: किमः क्षेपे

किमः क्षेपे (5.4.70)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_70_kimaH_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_70_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kimaH kzepe",
    text_dev              = "किमः क्षेपे",
    padaccheda_dev        = "किमः क्षेपे",
    why_dev               = "(सूत्रम् 5.4.70) किमः क्षेपे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
