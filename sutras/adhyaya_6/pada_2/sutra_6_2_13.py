"""
6.2.13  गन्तव्यपण्यं वाणिजे  —  VIDHI

Padaccheda: गन्तव्य-पण्यम् वाणिजे

गन्तव्यपण्यं वाणिजे (6.2.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_13_gantavyapa_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gantavyapaRyaM vARije",
    text_dev              = "गन्तव्यपण्यं वाणिजे",
    padaccheda_dev        = "गन्तव्य-पण्यम् वाणिजे",
    why_dev               = "(सूत्रम् 6.2.13) गन्तव्यपण्यं वाणिजे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
