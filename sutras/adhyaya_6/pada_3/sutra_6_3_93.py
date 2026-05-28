"""
6.3.93  समः समि  —  VIDHI

Padaccheda: समः समि (लुप्तप्रथमान्तनिर्देशः)

समः समि (6.3.93)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_93_samaH_93"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.93"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samaH sami",
    text_dev              = "समः समि",
    padaccheda_dev        = "समः समि (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = "(सूत्रम् 6.3.93) समः समि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
