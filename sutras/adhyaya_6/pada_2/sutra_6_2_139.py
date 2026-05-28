"""
6.2.139  गतिकारकोपपदात् कृत्  —  VIDHI

Padaccheda: गति-कारक-उपपदात् कृत्

गतिकारकोपपदात् कृत् (6.2.139)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_139_gatikArako_139"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.139"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.139",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gatikArakopapadAt kft",
    text_dev              = "गतिकारकोपपदात् कृत्",
    padaccheda_dev        = "गति-कारक-उपपदात् कृत्",
    why_dev               = "(सूत्रम् 6.2.139) गतिकारकोपपदात् कृत्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
