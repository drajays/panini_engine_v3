"""
4.1.167  यूनश्च कुत्सायाम्  —  VIDHI

Padaccheda: यूनः च कुत्सायाम्

यूनश्च कुत्सायाम् (4.1.167)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_167_yUnaSca_167"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_167_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.167"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yUnaSca kutsAyAm",
    text_dev              = "यूनश्च कुत्सायाम्",
    padaccheda_dev        = "यूनः च कुत्सायाम्",
    why_dev               = "(सूत्रम् 4.1.167) यूनश्च कुत्सायाम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
