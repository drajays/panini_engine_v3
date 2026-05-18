"""
7.2.81  आतो ङितः  —  VIDHI

Padaccheda: आतः ङितः

आतो ङितः (7.2.81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_81_Ato_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_81_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ato NitaH",
    text_dev              = "आतो ङितः",
    padaccheda_dev        = "आतः ङितः",
    why_dev               = "(सूत्रम् 7.2.81) आतो ङितः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
