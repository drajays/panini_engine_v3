"""
6.2.57  कतरकतमौ कर्मधारये  —  VIDHI

Padaccheda: कतर-कतमौ कर्मधारये

कतरकतमौ कर्मधारये (6.2.57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_57_katarakata_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "katarakatamO karmaDAraye",
    text_dev              = "कतरकतमौ कर्मधारये",
    padaccheda_dev        = "कतर-कतमौ कर्मधारये",
    why_dev               = "(सूत्रम् 6.2.57) कतरकतमौ कर्मधारये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
