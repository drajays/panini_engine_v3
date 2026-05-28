"""
6.1.14  बन्धुनि बहुव्रीहौ  —  VIDHI

Padaccheda: बन्धुनि बहुव्रीहौ

बन्धुनि बहुव्रीहौ (6.1.14)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_14_banDuni_14"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "banDuni bahuvrIhO",
    text_dev              = "बन्धुनि बहुव्रीहौ",
    padaccheda_dev        = "बन्धुनि बहुव्रीहौ",
    why_dev               = "(सूत्रम् 6.1.14) बन्धुनि बहुव्रीहौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
