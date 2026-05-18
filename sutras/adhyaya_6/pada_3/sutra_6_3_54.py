"""
6.3.54  हिमकाषिहतिषु च  —  VIDHI

Padaccheda: हिम-काषि-हतिषु च

हिमकाषिहतिषु च (6.3.54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_54_himakAziha_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_54_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "himakAzihatizu ca",
    text_dev              = "हिमकाषिहतिषु च",
    padaccheda_dev        = "हिम-काषि-हतिषु च",
    why_dev               = "(सूत्रम् 6.3.54) हिमकाषिहतिषु च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
