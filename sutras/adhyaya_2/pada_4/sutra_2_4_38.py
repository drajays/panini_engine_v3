"""
2.4.38  घञपोश्च  —  VIDHI

Padaccheda: घञ्-अपोः च

Also with ghan and ap suffixes.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_38_ghana_apah_ca"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_38_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "GaYapoSca",
    text_dev              = "घञपोश्च",
    padaccheda_dev        = "घञ्-अपोः च",
    why_dev               = "घञ्-अपोः च (२.४.३८)।",
    anuvritti_from        = ('2.4.35',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
