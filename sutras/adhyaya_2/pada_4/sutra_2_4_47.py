"""
2.4.47  सनि च  —  VIDHI

Padaccheda: सनि च

Also in san (desiderative).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_47_sani_ca"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.47", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sani ca",
    text_dev              = "सनि च",
    padaccheda_dev        = "सनि च",
    why_dev               = "सनि च (२.४.४७)।",
    anuvritti_from        = ('2.4.46',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
