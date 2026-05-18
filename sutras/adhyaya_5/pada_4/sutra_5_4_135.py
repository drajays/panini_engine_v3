"""
5.4.135  गन्धस्येदुत्पूतिसुसुरभिभ्यः  —  VIDHI

Padaccheda: गन्धस्य इत् उत्-पूति-सु-सुरभिभ्यः

गन्धस्येदुत्पूतिसुसुरभिभ्यः (5.4.135)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_135_ganDasyedu_135"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_135_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.135"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.135",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ganDasyedutpUtisusuraBiByaH",
    text_dev              = "गन्धस्येदुत्पूतिसुसुरभिभ्यः",
    padaccheda_dev        = "गन्धस्य इत् उत्-पूति-सु-सुरभिभ्यः",
    why_dev               = "(सूत्रम् 5.4.135) गन्धस्येदुत्पूतिसुसुरभिभ्यः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
