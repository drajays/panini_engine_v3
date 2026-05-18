"""
4.2.69  तस्य निवासः  —  VIDHI

Padaccheda: तस्य निवासः

तस्य निवासः (4.2.69)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_69_tasya_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_69_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasya nivAsaH",
    text_dev              = "तस्य निवासः",
    padaccheda_dev        = "तस्य निवासः",
    why_dev               = "(सूत्रम् 4.2.69) तस्य निवासः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
