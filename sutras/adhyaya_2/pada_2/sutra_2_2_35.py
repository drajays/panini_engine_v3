"""
2.2.35  सप्तमीविशेषणे बहुव्रीहौ  —  VIDHI

Padaccheda: सप्तमी-विशेषणे बहुव्रीहौ

Saptami used as visesana in bahuvrihi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_35_saptami_visesana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("bahuvrIhi" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["bahuvrihi_kind"]             = "2.2.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saptamIviSezaRe bahuvrIhO",
    text_dev              = "सप्तमीविशेषणे बहुव्रीहौ",
    padaccheda_dev        = "सप्तमी-विशेषणे बहुव्रीहौ",
    why_dev               = "सप्तमी-विशेषणे बहुव्रीहौ (२.२.३५)।",
    anuvritti_from        = ('2.2.23',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
