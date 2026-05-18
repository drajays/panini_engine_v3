"""
4.2.27  अपोनप्त्रपान्नप्तृभ्यां घः  —  VIDHI

Padaccheda: अपोनप्तृ-अपान्नप्तृभ्याम् घः

अपोनप्त्रपान्नप्तृभ्यां घः (4.2.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_27_aponaptrap_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_27_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aponaptrapAnnaptfByAM GaH",
    text_dev              = "अपोनप्त्रपान्नप्तृभ्यां घः",
    padaccheda_dev        = "अपोनप्तृ-अपान्नप्तृभ्याम् घः",
    why_dev               = "(सूत्रम् 4.2.27) अपोनप्त्रपान्नप्तृभ्यां घः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
