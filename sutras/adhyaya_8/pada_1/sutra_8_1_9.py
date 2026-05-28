"""
8.1.9  एकं बहुव्रीहिवत्  —  VIDHI

Padaccheda: एकम् बहुव्रीहि-वत्

एकं बहुव्रीहिवत् (8.1.9)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_9_ekaM_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_9_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekaM bahuvrIhivat",
    text_dev              = "एकं बहुव्रीहिवत्",
    padaccheda_dev        = "एकम् बहुव्रीहि-वत्",
    why_dev               = "(सूत्रम् 8.1.9) एकं बहुव्रीहिवत्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
