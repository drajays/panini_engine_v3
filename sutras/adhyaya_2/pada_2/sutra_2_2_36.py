"""
2.2.36  निष्ठा  —  VIDHI

Padaccheda: निष्ठा

Nistha-suffix form in bahuvrihi compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_36_nistha_bahuvrihi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("bahuvrIhi" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["bahuvrihi_kind"]             = "2.2.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizWA",
    text_dev              = "निष्ठा",
    padaccheda_dev        = "निष्ठा",
    why_dev               = "निष्ठा-अन्तं बहुव्रीहौ (२.२.३६)।",
    anuvritti_from        = ('2.2.23',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
