"""
8.1.8  वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सनभर्त्सनेषु  —  VIDHI

Padaccheda: वाक्य-आदेः आमन्त्रितस्य असूया-सम्मति-कोप-कुत्सन-भर्त्सनेषु

वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सनभर्त्सनेषु (8.1.8)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_8_vAkyAderAm_8"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_8_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAkyAderAmantritasyAsUyAsammatikopakutsanaBartsanezu",
    text_dev              = "वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सनभर्त्सनेषु",
    padaccheda_dev        = "वाक्य-आदेः आमन्त्रितस्य असूया-सम्मति-कोप-कुत्सन-भर्त्सनेषु",
    why_dev               = "(सूत्रम् 8.1.8) वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सनभर्त्सनेषु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
